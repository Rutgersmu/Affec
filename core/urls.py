from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.intro, name="intro"),
    path('home/', views.home, name="home"),
    path('home/request', views.query, name='query')
]