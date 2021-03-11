import os
import sys

import requests

sys.path.append(os.getcwd())

from .db.models import User, Message, session_scope
from .utils.sorter import sorter_list_by_key as sorter
from .utils.dict_mod import dict_extractor, dict_val_conv, dict_date_conv
from .logging_setup.setup_logger import logger


class LogWorker:
    """
    Обработчик логов, получаемых по http.
    Рботает с форматом json.
    """

    def __init__(self, url: str, url_param: str):
        """
        Конструктор, принимающий адрес url и параметр для получения данных.

        """
        self.__url = url
        self.__url_param = url_param
        self.conn_line = f'{self.__url}{self.__url_param}'

    def get_site_data(self) -> list:
        """
        Получение логов с указанного ресурса.
        Данные сохраняются в списке self.logs.
        """
        try:
            request = requests.get(self.conn_line).json()
            self.all_logs = request
        except requests.ConnectionError as err:
            print("***Error has occurred.\nDoes this resource support fetching json data?", err, sep='\n')
            return None
        else:
            if self.all_logs['error']:
                print(f'*** Error has occurred:\n{self.all_logs["error"]}')
                return None

            # Список словарей с логами
            self.logs = self.all_logs['logs']
            logger.info('Class LogWorker received log data')

            return self.logs

    def sort_data(self, dict_key: str = 'created_at'):
        """Сортировка данных по указанному ключу словаря
        (дата по умолчанию)."""
        try:
            self.logs = sorter(self.logs, dict_key)
        except AttributeError as err:
            message = """Did you get the resourse data?
            To receive, execute <obj_name>.get_site_data()."""
            print(message, f'\n\n***Error: {err}')

    def write_to_db(self):
        """Подготавливает данные и записывает их в базу данных."""
        # Преобразование строк в числа по указанным полям
        clean_data = dict_val_conv(self.logs, 'user_id')
        # Преобразование времени в объектах сообщений
        clean_data = dict_date_conv(clean_data, 'created_at')

        # Разделение пользовательских данных и сообщений
        user_data = dict_extractor(clean_data,
                                   'first_name',
                                   'second_name',
                                   'user_id')

        mes_data = dict_extractor(clean_data,
                                  'created_at',
                                  'message',
                                  'user_id')

        # Создание объектов пользователей и сообщений
        users = [User(user_id=user_obj['user_id'],
                      first_name=user_obj['first_name'],
                      second_name=user_obj['second_name'], )
                 for user_obj in user_data]

        messages = [Message(user_id=mes_obj['user_id'],
                            body=mes_obj['message'],
                            created_at=mes_obj['created_at'], )
                    for mes_obj in mes_data]

        # Запись пользователей в БД
        for user in users:
            with session_scope() as session:
                session.add(user)
        # Запись сообщений в БД
        with session_scope() as session:
            session.add_all(messages)
        logger.info('Class LogWorker wrote the logs to the database')
