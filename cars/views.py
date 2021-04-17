from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView
from rest_framework import viewsets

from cars.models import Car
from cars.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


def list_car(request):
    return render(request,'cars/list_car.html',
                  {'cars':Car.objects.all()})

def detail_car(request, slug):
    car = get_object_or_404(Car, slug=slug)
    return render(request, 'cars/detail_car.html', {'car': car})

class Detail(DetailView):
    model = Car
    template_name = 'cars/detail_car.html'
    slug_field = 'url'