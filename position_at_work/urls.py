from django.urls import path
from position_at_work import views


urlpatterns = [
    path('', views.PositionAtWorkView.as_view()),
    path('<int:pk>/', views.PositionAtWorkDetailView.as_view()),
]
