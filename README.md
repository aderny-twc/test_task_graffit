# Программа работы с логами (тестовое задание)

Класс для получения логов со стороннего ресурса, обработки их и сохранения в локальную базу данных.

## Установка и настройка окружения

```
$ git clone https://github.com/aderny-twc/test_task_graffit.git
$ cd test_taks_graffit
$ python -m venv venv
$ . venv/bin/activate
```

Установка зависимостей

```
(venv) pip install -r requirements.txt
```

## Запуск программы

Параметры ресурса задются в конструкторе класса

```python
# Адрес
URL = 'http://www.dsdev.tech/logs/'
# Дата:
URL_KEY = '20210123'

# Объект класса
some_logs = LogWorker(URL, URL_KEY)
```

Класс `LogWorker()` предоставляет методы для:

- Получения логов с ресурса
- Сортировки логов по дате
- Запись данных в БД

Пример использования - файл `main.py`

```
(venv) pyhton main.py
```

## Структура проекта

```
test_task_graffit/
├── docs
│   ├── db_schema.txt
│   └── descr.md
├── LICENSE
├── logger
│   ├── db
│   │   ├── __init__.py
│   │   └── models.py
│   ├── __init__.py
│   ├── logger.py
│   ├── logging_setup
│   │   ├── __init__.py
│   │   └── setup_logger.py
│   └── utils
│       ├── dict_mod.py
│       ├── __init__.py
│       └── sorter.py
├── main.py
├── README.md
├── requirements.txt
└── tests
    └── unit_tests.py
```

`docs/` - содержит документы и описание решенных задач
`logger/` - главная директория проекта. Содержит директории для работы с БД, логированием, и дополнительными утилитами.

## Описание работы

Файл `models.py` описывает модели для хранения в БД, используется SQLAlchemy. Также, он представляет контекстный менеджер для работы с сессиями. Структура БД описана в `docs/db_schema.txt`.

Файл `logging_setup/setup_logger.py` содержит файл с настройками логирования работы класса `LogWorker()`.

Директория `utils/` содержит дополнительные функции для работы класса. `dict_mod.py` содержит функции для обработки данных в логах. Файл `sorter.py` содержит функцию для сортировки списка словарей по выбранной строке (сортировка вставками).

Класс `LogWorker()` в файле `logger.py` принимает url и дату в качестве параметров.
Метод `get_site_data()` обращается по указанному ресурсу, получает json и возвращает словарь с логами.
Метод sort_data() модифицирует логи с использованием функции `sorter_list_by_key`, сортируя логи по дате.
Метод `write_to_db()` обрабатывает данные логов, создает объекты моделей, и, впоследствии, записывает их в БД.

