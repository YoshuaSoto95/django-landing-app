from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.home, name='home'),
    path('thankyou_page/', views.thankyou_page, name='thankyou_page'),
    path('capture_lead/', views.capture_lead, name='capture_lead'),
]
