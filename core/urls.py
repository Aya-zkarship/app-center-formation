from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devis/', views.devis, name='devis'),
    path('login-client/', views.client_login, name='client_login'),
    path('client/', views.client_dashboard, name='client_dashboard'),
    path('update-progress/<int:inscription_id>/', views.update_progress, name='update_progress'),
    path('logout/', views.logout_view, name='logout'),
]   