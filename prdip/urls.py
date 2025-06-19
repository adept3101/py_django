"""
URL configuration for prdip project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from users import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='main/')),
    path('main/', views.page, name='main'),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('fincert/', views.FincertView.as_view(), name='fincert'),
    path('mvd/', views.MVDViews.as_view(), name='mvd'),
    path('ioc/', views.IOCViews.as_view(), name='ioc'),
    path('delete_accounts/', views.delete_accounts, name='delete_accounts'),
]