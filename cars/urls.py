from django.urls import path

from cars.views import list_car, detail_car, cars_app, list_car_published

urlpatterns = [
    path('',list_car, name='list_car'),
    path('cars_published/', list_car_published, name='list_car_published'),
    path('cars_app/', cars_app, name='cars_app'),
    path('<slug:slug>/',detail_car, name='detail_car'),

]