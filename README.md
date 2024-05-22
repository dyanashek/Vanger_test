# Fake-nasa landing page
***
Лэндинг со слайдером картинок, настраиваемым через админ-панель.

## Демо-версия:
1. Расположена по адресу: http://178.21.8.237:8000/
2. Админка по адресу: http://178.21.8.237:8000/admin/
3. **Логин:** vanger\
**Пароль:** 1234

## Установка и использование:
- Клонируйте репозиторий; перейдите в нужную директорию и выполните:
```sh
git clone https://github.com/dyanashek/Vanger_test
```
- Установите виртуальное окружение и активируйте его:
> Установка и активация в корневой папке проекта
```sh
python3 -m venv venv
source venv/bin/activate # for macOS
source venv/Scripts/activate # for Windows
```
- Установите зависимости: (из директории, содержащей req.pip)
```sh
pip install -r req.pip
```
- В директории vanger (содержащей файл manager.py) создайте .env, содержащий **DJANGO_KEY** (секретный ключ django), **DB_NAME**, **USER_NAME**, **USER_PASSWORD** (данные для подключения к бд MySQL)
- Совершите миграции и создайте суперпользователя: (из директории, содержащей manager.py)
```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
- Запустите проект (из директории, содержащей файл manage.py):
```sh
python3 manage.py runserver
```

