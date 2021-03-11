from unittest import TestCase, main
from unittest.mock import patch, Mock
import sys, os

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


class FakeJson:
    def __init__(self):
        self.json = json.dumps(fake_logs)
        fake_logs['error'] = 'some error'
        self.json_err = json.dumps(fake_logs)


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
        fake_json = Mock(return_value=FakeJson().json)
        logger.requests.get = fake_json
        result = logworker.get_site_data()
        self.assertEqual(result, fake_logs['logs'])

    def test_logworker_json_err_return_none(self):
        logworker = LogWorker('some_url', 'key')
        fake_json = Mock(return_value=FakeJson().json_err)
        logger.requests.get = fake_json
        result = logworker.get_site_data()
        self.assertEqual(result, None)


if __name__ == '__main__':
    main()