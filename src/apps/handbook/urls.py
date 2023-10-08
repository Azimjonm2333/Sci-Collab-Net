from django.urls import path

from src.apps.handbook.views import (
    TagListView,
    TagDetailView,
    CategoryListView,
    CategoryProjectView,
)

urlpatterns = [
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    path('categories/', CategoryListView.as_view(), name='category'),
    path('categories/projects/', CategoryProjectView.as_view(), name='create-projects-for-categories'),
]
