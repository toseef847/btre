from django.urls import path
from . import views

# app_name = 'listings'
urlpatterns = [
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('dashboard1', views.dashboard1, name = 'dashboard1'),
]
