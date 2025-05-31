# URL Shortener

Простой сервис сокращения URL на FastAPI с базой данных SQLite (по умолчанию).

## Установка и запуск локально (Windows CMD)

1. **Клонируйте репозиторий:**

```cmd
git clone <URL_репозитория>
cd impule
```

2. **Создайте и активируйте виртуальное окружение:**

```cmd
python -m venv venv
venv\Scripts\activate
```

3. **Установите зависимости:**

```cmd
pip install -r requirements.txt
```

4. **Создайте файл .env в корне проекта (если его нет):**

```cmd
DATABASE_URL=sqlite:///./shortener.db
```
5. **Запустите сервер:**

```cmd
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

6. **Откройте в браузере:**

```cmd
http://127.0.0.1:8000/docs
```
Там доступна интерактивная документация API.

Если хотите, можно запускать через Makefile (требуется установленный make):

```cmd
make run
```

7. **Авторизация:**

Для приватных эндпоинтов используйте Basic Auth:

```cmd
Логин: admin
Пароль: password
```

