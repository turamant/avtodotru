
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from cars.views import CarViewSet
from posters.views import list_posters, PosterViewSet

router = routers.SimpleRouter()
router.register('api/cars',CarViewSet)
router.register('api/posters',PosterViewSet)

urlpatterns = [
    path('',TemplateView.as_view(template_name='_base.html'),name='home'),
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('posters/',list_posters, name='list_posters'),
    path('api-auth/',include('rest_framework.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)