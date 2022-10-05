from django.urls import path
from . import views


#Urls
urlpatterns = [
   path('',views.index, name='all-meetups'),
   path('<slug:meetup_slug>/success', views.confirmation_registration, name='confirmation-registration'),
   path('<slug:meetup_slug>', views.meetup_details, name='meetup-details') 
]
