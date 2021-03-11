from logger.logger import LogWorker

# Пример использования класса работы с логами

# Адрес и ключ ресурса
URL = 'http://www.dsdev.tech/logs/'
URL_KEY = '20210123'


# Цикл обработки логов
def main():
    # Создание объкта работы с логами
    some_logs = LogWorker(URL, URL_KEY)

    # Получение данных с ресурса
    some_logs.get_site_data()

    # Сортировка данных
    some_logs.sort_data()

    # Запись данных в БД
    some_logs.write_to_db()


if __name__ == '__main__':
    main()
