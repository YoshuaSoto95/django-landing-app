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
]
