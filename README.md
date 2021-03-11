# Логгер (тестовое задание)

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

Пример использования - файл `main.py`

```
(venv) pyhton main.py
```

## Структура проекта

```

```

