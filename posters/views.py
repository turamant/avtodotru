from django.shortcuts import render

# Create your views here.
from posters.models import Poster


def list_posters(request):
    return render(request, 'posters/posters.html',{'posters':Poster.objects.all()})
