# Каталог автомобилей auto.ru

Мини проект, который позволяет просмотреть список марок автомобилей и выгрузить список моделей по определенной марке.

Когда база не заполнена, то необходимо нажать кнопку обновить каталог. С сайта auto.ru подтянутся все марки и автомобили и появится всплывающее окно, которое предупредит, что выгрузка завершена. Затем необходимо будет обновить страницу и тогда в выпадающем списке появятся все марки автомобилей. При выборе определенной марки и нажатии на кнопку показать модели, ниже появися список моделей выбранной марки.

### Стек технологий:

- Django
- Flake8
- python-dotenv
- requests
- xml.etree

### Начало работы
1. Установить зависимости командой `pip install -r requirements.txt`
1. Заполнить .env файл в соответствии с файлом `.env_sample`
2. Провести миграции командой `python manage.py migrate`
3. Запустить прложение командой `python manage.py runserver`
4. Сервис будет доступен локально адресу `http://127.0.0.1:8000/`