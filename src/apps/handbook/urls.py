from django.urls import path

from src.apps.handbook.views import (
    TagListView,
    TagDetailView,
    CategoryListView,
    CategoryProjectView,
    FavoritesListCreateView,
    FavoritesDestroyView,
    ChatListCreateView,
    ChatRetrieveUpdateDestroyView
)

urlpatterns = [
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    path('categories/', CategoryListView.as_view(), name='category'),
    path('categories/projects/', CategoryProjectView.as_view(), name='create-projects-for-categories'),
    
    path('favorites/', FavoritesListCreateView.as_view(), name='favorites-list-create'),
    path('favorites/<int:pk>/', FavoritesDestroyView.as_view(), name='favorites-delete'),
    
    path('chat/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('chat/<int:pk>/', ChatRetrieveUpdateDestroyView.as_view(), name='chat-delete'),
]
