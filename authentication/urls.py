from django.urls import path

from authentication.views import LoginAPIView, RegistrationAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),    
]
