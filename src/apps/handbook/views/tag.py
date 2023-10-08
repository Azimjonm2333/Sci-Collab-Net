from src.apps.handbook.models import Tag
from src.apps.handbook.serializers import (
    TagListSerializer,
    TagDetailSerializer,
)
from rest_framework import generics
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)


class TagListView(generics.ListAPIView):
    """ List api view for tag model """
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    authentication_classes = ()
    filter_backends = (
        SearchFilter,
        OrderingFilter
    )
    search_fields = (
        'name',
    )


class TagDetailView(generics.RetrieveAPIView):
    """ Detail api view for tag model """
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer
    authentication_classes = ()


    