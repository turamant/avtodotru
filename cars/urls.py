from django.urls import path

from cars.views import list_car, detail_car, Detail

urlpatterns = [
    path('',list_car, name='list_car'),
    #path('<slug:slug>/',detail_car, name='detail_car'),
    path('<slug:slug>/', Detail.as_view(), name='detail_car'),
]