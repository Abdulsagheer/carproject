from django.urls import path
from .views import cars,car_detail,search

app_name='cars'

urlpatterns = [

   path('',cars,name='cars'),
   path('<int:id>',car_detail,name='car_detail'),
   path('search',search,name='search'),

]
