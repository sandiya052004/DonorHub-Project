

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home/donation_requests', views.donation_requests, name='donation_requests'),
    path('home/create_donation_list/', views.create_donation_request, name='create_donation_request'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('signup/', views.signup, name='signup'),
    path('add_organization/', views.add_organization, name='add_organization'),
    
]

