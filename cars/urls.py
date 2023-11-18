from django.urls import path

from cars.apps import CarsConfig
from cars.views import update_autoru_catalog, index

app_name = CarsConfig.name

# Урлы приложения автомобилей
urlpatterns = [
    path('update_catalog', update_autoru_catalog, name='update_catalog'),
    path('', index, name='index'),
]
