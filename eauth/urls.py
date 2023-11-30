from django.urls import path
from eauth import views


urlpatterns = [
    path('login', views.login, name="login")
]