from src.apps.handbook.models import Category
from src.apps.handbook.serializers import NestedCategorySerializer, CategorySlugListSerializer
from src.apps.project.models import Project
from src.apps.project.serializers import ProjectDetailSerializer, ProjectListSerializer

from django.http import Http404
from rest_framework import generics
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q



class CategoryListView(generics.ListAPIView):
    """ List api view for category models """

    serializer_class = NestedCategorySerializer
    authentication_classes = ()
    filter_backends = (
        SearchFilter,
        OrderingFilter
    )
    search_fields = (
        'name',
    )

    def get_queryset(self):
        return Category.objects.filter(parent=None)





class CategoryProjectView(APIView):
    serializer_class = CategorySlugListSerializer
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = CategorySlugListSerializer(data=request.data)
        if serializer.is_valid():
            categories = serializer.validated_data['categories']

            query = Q()
            for category in categories:
                query |= Q(categories=category) | Q(categories__parent=category)

            projects = Project.objects.filter(query).distinct().order_by(
                '-downloads_count',
                '-likes_count',
                '-comments_count',
                '-views_count'
            )

            serializer = ProjectListSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Category does not exist"}, status=status.HTTP_400_BAD_REQUEST)
