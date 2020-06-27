from django.urls import path

import users.views as views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('password/change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
]
