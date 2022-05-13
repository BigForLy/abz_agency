from django.urls import path

from staff import views


urlpatterns = [
    path('staff_tree/', views.StaffTreeView.as_view()),
    path('staff/', views.StaffView.as_view()),
    path('staff/<int:pk>/', views.StaffDetailView.as_view()),
    path('position_at_work/', views.PositionAtWorkView.as_view()),
    path('position_at_work/<int:pk>/', views.PositionAtWorkDetailView.as_view()),
]
