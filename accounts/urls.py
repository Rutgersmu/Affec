from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.accounts_signup, name='signup'),
    path('login/', views.accounts_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('redirect/', lambda req: redirect('/')),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('mypage/user/', views.user, name='user'),

]

