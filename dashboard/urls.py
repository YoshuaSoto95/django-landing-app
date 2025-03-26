from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('change_password/<int:user_id>/', views.change_password, name='change_password'),

    path('leads/', views.leads, name='leads'),
    path('leads/edit_lead/<int:id>', views.edit_lead, name="edit_lead"),
    path('leads/delete_lead/<int:id>', views.delete_lead, name="delete_lead"),

    path('users/', views.users, name="users"),
    path('users/register_user/', views.register_user, name="register_user"),
    path('users/edit_user/<int:id>', views.edit_user, name="edit_user"),
    path('users/delete_user/<int:id>', views.delete_user, name="delete_user"),
    path('users/change_password_user/<int:id>', views.change_password_user, name="change_password_user"),

    path('analytics/', views.analytics, name="analytics"),

    path('config_profile/', views.config_profile, name="config_profile"),
]
