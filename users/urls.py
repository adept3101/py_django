from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('main/', views.page, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('fincert/', views.FincertView.as_view(template_name='users/fincert.html'), name='fincert'),
    path('mvd/', views.MVDViews.as_view(template_name='users/mvd.html'), name='mvd'),
    path('ioc/', views.IOCViews.as_view(template_name='users/ioc.html'), name='ioc'),
    path('delete/<str:model_name>/', views.delete, name='delete'),
    path('create/<str:model_name>/', views.create, name='create'),
]