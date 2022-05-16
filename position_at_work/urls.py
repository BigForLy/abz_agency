from django.urls import path
from position_at_work import views


urlpatterns = [
    path('position_at_work/', views.PositionAtWorkView.as_view()),
    path('position_at_work/<int:pk>/', views.PositionAtWorkDetailView.as_view()),
]
