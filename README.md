# Застрахуй братуху
Биржа продажи услуг страховых компаний.

## Основные возможности:
### Для страховых компаний (авторизованные пользователи):
- Личный кабинет с возможностью создания и редактирования своих продуктов с различными параметрами такими как процентные ставки, сроки, категории (недвижимость, авто, жизнь)
- Просмотр откликов пользователей на свои продукты
### Для покупателей (неавторизованные пользователи):
- Просмотр услуг от страховых компаний с возможностью фильтрации по различным параметрам
- Возможность оставлять отклики на продукты страховых компаний
- При создании отклика на страховой продукт, создателю продукта будет отправлено электронное письмо.

## Настройка email рассылок
За рассылку отвечает сервис [sendinblue.com](https://www.sendinblue.com/)

В файле `dev.env` обязательно заполнить `SENDINBLUE_API_KEY`

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

[*опционально*] Загрузка фикстур
```sh
python insu-bro-nce/manage.py loaddata fixtures.json
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
- [ ] Написать тесты
  - [x] users
  - [ ] insurance
- [x] Добавить фикстуры
- [x] Настроить админку
- [ ] Добавить боевой конфиг
- [ ] Развернуть проект ([pythonanywhere.com](https://www.pythonanywhere.com/), [heroku.com](https://www.heroku.com) или где-нибудь ещё)
- [x] Добавить очередь задач (celery + RabbitMQ)
- [ ] Добавить полнотекстовый поиск (Elasticsearch)
  - [x] Минимальная настройка...
  - [ ] В [InsuranceProductFilteredTableView](https://github.com/BPIlyich/insu-bro-nce/blob/8440d579e3c899552a1f885caff3571384ab9480/insu-bro-nce/insurance/views.py#L19) фильтрацию делать средствами `django-elasticsearch-dsl`
