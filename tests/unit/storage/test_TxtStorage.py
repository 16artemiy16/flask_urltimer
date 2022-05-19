from flask import Flask
from unittest.mock import patch, mock_open

from flask_urltimer.storage.TxtStorage import TxtStorage


class TestImport:
    """ Test TxtStorage -> App import """

    def test_success(self):
        """
        GIVEN app instance and TxtStorage
        WHEN trying to import via TxtStorage
        THEN read appropriate file and return it's content as a list
        """
        app = Flask(__name__)

        filename = 'timings.txt'
        filepath = f'{app.root_path}/{filename}'

        mocked_text = '''{"first": 1, "second": "hi"}
{"first": 2, "second": "hello"}'''

        with patch('builtins.open', new=mock_open(read_data=mocked_text)) as _file:
            data = TxtStorage(app).importt()
            _file.assert_called_once_with(filepath, 'r')
            assert data == [dict(first=1, second='hi'), dict(first=2, second='hello')]
