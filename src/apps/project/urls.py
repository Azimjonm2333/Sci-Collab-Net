from django.urls import path

from src.apps.project.views import (
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
    ApplicationListCreateView,
    ApplicationRetrieveUpdateDestroyView,
    ApplicationApproveView
)

urlpatterns = [
    path('project/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('project/<str:slug>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),

    path('applications/', ApplicationListCreateView.as_view(), name='applications-list-create'),
    path('applications/<int:pk>/', ApplicationRetrieveUpdateDestroyView.as_view(), name='applications-detail'),
    path('applications/approve/', ApplicationApproveView.as_view(), name='applications-approve'),
]
