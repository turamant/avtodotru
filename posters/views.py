from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from posters.models import Poster
from posters.serializers import PosterSerializer


class PosterViewSet(viewsets.ModelViewSet):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer


def list_posters(request):
    return render(request, 'posters/posters.html',{'posters':Poster.objects.all()})
