"""
URL configuration for ecourt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from eauth import views
from case.views import dasboard

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('dashboard'))),
    path('dashboard/', dasboard, name="dashboard"),
    path('admin/', admin.site.urls),
    path('accounts/login/', views.login_create, name="login"),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/change-password', views.change_password, name='change-password'),
    path('case/', include('case.urls')),
    path('filing/', include('filing.urls')),
    path('registration/', include('registration.urls')),
    path('digitization', include('digitiz.urls')),
    path("select2/", include("django_select2.urls")),
]
