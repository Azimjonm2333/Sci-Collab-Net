from django.urls import path
from src.apps.post_info.views import (
    CommentListCreateView,
    CommentDestroyView,
    LikeListCreateView,
)


urlpatterns = [
    path('likes/', LikeListCreateView.as_view(), name='likes-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDestroyView.as_view(), name='comment-destroy'),
]
