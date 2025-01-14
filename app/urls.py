from django.urls import path, include
from app.views import UserRegistrationView,UserLoginView, UserProfileView, UserChangePassword, SendPasswordResetEmailView, UserPasswordResetView
urlpatterns = [
   path('register/', UserRegistrationView.as_view(), name = 'register'),
   path('login/', UserLoginView.as_view(), name = 'login'),
    path('profile/', UserProfileView.as_view(), name = 'profile'),
    path('changepassword/', UserChangePassword.as_view(), name = 'changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name = 'send-reset-password-email'),
    path('rest-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]