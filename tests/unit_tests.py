import os
import sys
from unittest import TestCase, main
from unittest.mock import patch, Mock

sys.path.append(os.getcwd())
from logger.logger import *
from logger import logger


fake_logs = {
    'error': '',
    'logs': [
        {
            'created_at': '2021-01-23T07:54:27',
            'first_name': 'John',
            'message': 'Oh, hi Mark!',
            'second_name': 'Doe',
            'user_id': '617919',
        },
        {
            'created_at': '2021-01-23T07:45:55',
            'first_name': 'Luke',
            'message': 'What happend?',
            'second_name': 'Smith',
            'user_id': '617233',
        },
    ]
}

fake_logs_error = {'error': 'Some error happened'}


class MockResponse:
    def __init__(self):
        self.json_data = None
        self.status_code = 200

    def json(self):
        return self.json_data


class TestLogger(TestCase):
    @patch('logger.logger.LogWorker')
    def test_logworker_get_site_data(self, MockLogWorker):
        logworker = MockLogWorker('some_url', 'key')
        logworker.get_site_data.return_value = fake_logs['logs']
        response = logworker.get_site_data()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

    def test_logworker_getting_json(self):
        logworker = LogWorker('some_url', 'key')
        fake_response = MockResponse()
        fake_response.json_data = fake_logs
        logger.requests.get = Mock(return_value=fake_response)
        result = logworker.get_site_data()
        self.assertEqual(result, fake_logs['logs'])

    def test_logworker_json_err_return_none(self):
        logworker = LogWorker('some_url', 'key')
        fake_response = MockResponse()
        fake_response.json_data = fake_logs_error
        logger.requests.get = Mock(return_value=fake_response)
        result = logworker.get_site_data()
        self.assertEqual(result, None)


if __name__ == '__main__':
    main()
