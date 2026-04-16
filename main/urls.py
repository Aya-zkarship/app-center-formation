from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devis/', views.devis_view, name='devis'),
    path('login-client/', views.client_login, name='login_client'),
    path('client/', views.client_dashboard, name='client_dashboard'),
    path('admin-page/', views.admin_page, name='admin_page'),
]