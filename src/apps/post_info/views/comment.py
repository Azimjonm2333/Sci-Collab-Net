from rest_framework.response import Response
from src.apps.post_info.models import Comment
from src.apps.post_info.serializers import (
    NestedCommentSerializer,
    CommentCreateSerializer
)
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated




class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = NestedCommentSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('message',)

    def get_queryset(self):
        if self.request.method == 'GET':
            return Comment.objects.filter(parent=None)
        elif self.request.method == 'POST':
            return Comment.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return NestedCommentSerializer
        elif self.request.method == 'POST':
            return CommentCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.project.update_comments_count()
        return Response(NestedCommentSerializer(instance).data, status=status.HTTP_201_CREATED)


class CommentDestroyView(generics.DestroyAPIView):
    
    serializer_class = NestedCommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        instance.project.update_comments_count()
        instance.delete()
