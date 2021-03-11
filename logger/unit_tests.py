import os
import sys
from unittest import TestCase, main
from unittest.mock import patch

sys.path.append(os.getcwd())


class TestLogger(TestCase):
    @patch('logger.LogWorker')
    def test_logworker_get_site_data(self, MockLogWorker):
        logworker = MockLogWorker('some_url', 'key')

        logworker.get_site_data.return_value = [
                    {
                        'created_at': '2021-01-23T07:54:27',
                        'first_name': 'John',
                        'message': 'Oh, hi Mark!',
                        'second_name': 'Doe',
                        'user_id': '617919',
                    },
                                        {    
                        'created_at': '2021-01-23T07:54:27',
                        'first_name': 'John',
                        'message': 'Oh, hi Mark!',
                        'second_name': 'Doe',
                        'user_id': '617919',
                    },
                ]
        response = logworker.get_site_data()
        self.assertInNotNone(response)
        self.assertIsInstance(response[0], dict)


if __name__ == '__main__':
    main()
