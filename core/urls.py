from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.intro, name="intro"),
    path('fun/', views.fun, name="fun"),
    path('fun/request', views.query, name='fun_query')
]