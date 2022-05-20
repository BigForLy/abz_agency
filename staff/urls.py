from django.urls import path
from staff import views


urlpatterns = [
    path('tree/', views.StaffTreeView.as_view()),
    path('', views.StaffView.as_view()),
    path('<int:pk>/', views.StaffDetailView.as_view()),
]
