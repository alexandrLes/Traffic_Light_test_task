# Traffic_Light_test_task
Test Task for Traffic Light

Это тестовое задание на Django для отображения древовидной структуры отделов с списком сотрудников. Проект использует Twitter Bootstrap для улучшения визуализации.

## Требования

- Python 3.8+
- Django 3.5+
- SQLite (по умолчанию)

## Установка

Следуйте этим шагам для настройки и запуска проекта на локальной машине.

### Клонирование репозитория

Склонируйте репозиторий к себе на машину:

```bash
git clone https://github.com/alexandrLes/Traffic_Light_test_task.git
cd Traffic_Light_test_task
python -m venv env
source env/bin/activate   # Для Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Откройте браузер и перейдите по адресу http://127.0.0.1:8000/departments/, чтобы увидеть древовидную структуру отделов и сотрудников.

### Заполнение базы данных

На данный момент база данных заполнена на 50000 данных при помощи библиотеки Fakes. Скрипт заполнения лежит в Traffic_Light_test_task/employees/management/commands/populate_db.py