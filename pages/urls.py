from django.urls import path
from .views import home,about,services,contact

app_name='pages'

urlpatterns = [
    path('',home,name='home'),
    path('about',about,name='about'), 
    path('services',services,name='services'), 
    path('contact',contact,name='contact'),

]
