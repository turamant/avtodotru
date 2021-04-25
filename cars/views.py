from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView
from rest_framework import viewsets

from cars.forms import CommentForm
from cars.models import Car
from cars.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


def list_car(request):
    return render(request,'cars/list_car.html',
                  {'cars':Car.objects.all()})

def list_car_published(request):
    return render(request, 'cars/list_car_published.html',
                  {'cars_published':Car.objects.filter(is_published=True, is_deleted=False)})

#rendering from vue.js
def cars_app(request):
    return render(request,'cars/cars_app.html')

def detail_car(request, slug):
    car = get_object_or_404(Car, url=slug)
    comments = car.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'cars/detail_car.html', {'car': car,
                                                    'comments':comments,
                                                    'new_comment':new_comment,
                                                    'comment_form':comment_form})

class Detail(DetailView):
    model = Car
    template_name = 'cars/detail_car.html'
    slug_field = 'url'

