import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")  # Замените myproject на имя вашего проекта
django.setup()

from my_site.models import user  # Замените myapp на имя вашего приложения

users_data = [
    {"name": "Иван Иванов", "email": "ivan@example.com", "city": "Москва", "login": "@IvanIvanov", "password": "pass123", "about_oneself": "Люблю путешествовать."},
    {"name": "Мария Смирнова", "email": "maria@example.com", "city": "Санкт-Петербург", "login": "@MariaSm", "password": "pass456", "about_oneself": "Обожаю котиков."},
    {"name": "Алексей Кузнецов", "email": "alex@example.com", "city": "Казань", "login": "@AlexK", "password": "pass789", "about_oneself": "Фанат футбола."}
]

for user_data in users_data:
    User = user(**user_data)
    User.save()

print("База данных заполнена!")
