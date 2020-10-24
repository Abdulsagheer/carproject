from django.urls import path
from .views import enquiry

app_name='contacts'

urlpatterns = [
    path('enquiry',enquiry,name='enquiry')

]