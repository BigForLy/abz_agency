from django.urls import path
from staff import views


urlpatterns = [
    path('staff_tree/', views.StaffTreeView.as_view()),
    path('staff/', views.StaffView.as_view()),
    path('staff/<int:pk>/', views.StaffDetailView.as_view()),
]
