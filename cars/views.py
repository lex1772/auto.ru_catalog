from django.http import HttpResponse

from cars.services import (
    get_file_from_autoru, delete_all_data, get_brands_and_models)


def update_autoru_catalog(request):
    """Контроллер для очистки файла и получения новых записей"""
    delete_all_data()
    get_file_from_autoru()
    return HttpResponse('Выполнено')


def index(request):
    """Контроллер для главной страницы"""
    return get_brands_and_models(request)
