# Застрахуй братуху
Биржа продажи услуг страховых компаний.

## Основные возможности:
### Для страховых компаний (авторизованные пользователи):
- Личный кабинет с возможностью создания и редактирования своих продуктов с различными параметрами такими как процентные ставки, сроки, категории (недвижимость, авто, жизнь)
- Просмотр откликов пользователей на свои продукты
### Для покупателей (неавторизованные пользователи):
- Просмотр услуг от страховых компаний с возможностью фильтрации по различным параметрам
- Возможность оставлять отклики на продукты страховых компаний

## Установка и запуск
### С помощью Docker
Сборка и первоначальный запуск
```sh
docker-compose up --build
```

Запуск тестов (пока не написаны)
```sh
docker-compose exec web python insu-bro-nce/manage.py test
```

Для создания суперпользователя
```sh
docker-compose exec web python insu-bro-nce/manage.py createsuperuser
```

После запуска докера сайт будет доступен по адресу `http://127.0.0.1:8080/`

### Без использования Docker
[*опционально*] Создаем виртуальное окружение
```sh
python3 -m venv .env
```

[*опционально*] Активируем виртуальное окружение
```sh
source .env/bin/activate
```

Устанавливаем зависимости
```sh
pip install -r requirements.txt
```

Миграции БД
```sh
python insu-bro-nce/manage.py migrate
```

Локализация
```sh
python insu-bro-nce/manage.py compilemessages
```

Запуск dev-сервера
```sh
python insu-bro-nce/manage.py runserver
```

## TODO
- Написать тесты
