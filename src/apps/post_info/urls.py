from django.urls import path
from src.apps.post_info.views import (
    CommentListCreateView,
    CommentDestroyView,
    LikeListCreateView,
    ViewListCreateView,
    DownloadListCreateView,
)


urlpatterns = [
    path('likes/', LikeListCreateView.as_view(), name='likes-list-create'),
    path('views/', ViewListCreateView.as_view(), name='views-list-create'),
    path('downloads/', DownloadListCreateView.as_view(), name='downloads-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDestroyView.as_view(), name='comment-destroy'),
]
