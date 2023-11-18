import xml.etree.ElementTree as ET

import requests
from django.shortcuts import render

from cars.models import Brand, Model


# Бизнес логика приложения
def delete_all_data():
    """Функция удаления всех записей в базе данных"""
    Brand.objects.all().delete()
    Model.objects.all().delete()


def brand_save(brand_id: int, brand: str):
    """Функция сохранения марки автомобиля в базе данных"""
    brand = Brand(id=brand_id, name=brand)
    brand.save()


def model_save(model_id: int, brand: int, model: str):
    """Функция сохранения модели автомобиля в базе данных"""
    brand = Model(id=model_id, brand=Brand.objects.get(pk=brand), name=model)
    brand.save()


def get_file_from_autoru():
    """Функция получения данных из xml файла
    и преобразования этих данных в нужные по заданию"""
    response = requests.get(
        "https://auto-export.s3.yandex.net/auto/price-list/catalog/cars.xml")
    tree = ET.fromstring(response.text)
    marks = tree.findall('mark')
    brand_id = 0
    model_id = 0
    for mark in marks:
        brand_id += 1
        mark_name = mark.attrib['name']
        brand_save(brand_id, mark_name)

        folders = mark.findall('.//folder')
        models_list = []
        for folder in folders:
            model_id += 1
            folder_name = folder.attrib['name'].split(',')[0].strip()
            if folder_name not in models_list:
                models_list.append(folder_name)
                model_save(model_id, brand_id, folder_name)


def get_brands_and_models(request):
    """Функция для получения марок и моделей автомобилей на главной странице"""
    brands = Brand.objects.all().order_by("name")
    if request.method == 'GET':
        selected_brand = request.GET.get('brand')
        if selected_brand:
            models = Model.objects.filter(
                brand__name=selected_brand).order_by("name")
        else:
            models = None
    else:
        models = None

    return render(
        request,
        'cars/index.html',
        {'brands': brands, 'models': models})
