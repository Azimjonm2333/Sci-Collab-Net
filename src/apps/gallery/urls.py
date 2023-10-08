from django.urls import path, include
from rest_framework import routers

from src.apps.gallery.views import (
    FolderAPIView,
    ImageAPIView,
    FolderImageAPIView
)

router = routers.DefaultRouter()
router.register(r'folders', FolderAPIView)
router.register(r'images', ImageAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('folders/<int:pk>/images', FolderImageAPIView.as_view(), name='folder-image'),
]
