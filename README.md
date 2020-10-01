# TODO API

### Что ты такое?

REST api персонализированного сервиса, позволяющего пользователю ставить себе задачи, изменять их статус и передвигать дедлайн (осуждаю за это). 

### Немного про API:

```
/api/v1/register/ - регистрация пользователя по логину и паролю (POST)
/api/v1/token/ - получить токен по логину и паролю (POST)
/api/v1/tasks/ - список всех задач пользователя (GET)
/api/v1/tasks/ - создать задачу, необходимо передать title, description, status и deadline (POST)
/api/v1/tasks/<int:task_id>/ - просмотр конкретной задачи по ее id (GET)
/api/v1/tasks/<int:task_id>/ - изменение/удаление конкретной задачи по ее id (PUT, PATCH, DELETE)
/api/v1/tasks/<int:task_id>/change_history/ - просмотр истории изменений задачи (GET)
```

### Как запустить?

Склонируйте репозиторий:

```bash
git clone https://github.com/sh4rpy/todo_api.git
```

Создайте файл .env в одной директории с файлом settings.py. Создайте в нем переменную окружения  SECRET_KEY, которой присвойте скопированный ключ с [сайта генерации ключей](https://djecrety.ir). Далее добавьте переменные для работы с базой данных. Выглядеть файл должен так:

```python
SECRET_KEY=скопированный_ключ
DB_ENGINE=django.db.backends.postgresql
DB_NAME=имя_базы
DB_USER=юзернейм
DB_PASSWORD=пароль
DB_HOST=db # имя контейнера базы данных
DB_PORT=порт
```

Запустите **docker-compose** командной:

```bash
docker-compose up
```

Сервис станет доступен по адресу [http://0.0.0.0:8000](http://0.0.0.0:8000).