from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('register_user', views.register_user),
    path('login_user', views.login_user),
    path('logout', views.logout)
]