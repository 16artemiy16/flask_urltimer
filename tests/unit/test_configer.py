import pytest
from flask import Flask
from flask_urltimer.configer import *


def test_constants():
    """
    All constants should be properly set.
    """
    assert URLTIMER_URL_PATH == 'URLTIMER_URL_PATH'
    assert defaults[URLTIMER_URL_PATH] == 'timings-ui'


class TestGetByKey:
    """ get_by_key() function should work correctly """
    def test_get_set_value(self):
        """
        GIVEN a prop set in the app config
        WHEN trying to get the prop by a key
        THEN return this prop
        """
        app = Flask(__name__)
        app.config['URLTIMER_URL_PATH'] = 'test123'
        assert get_by_key(app, URLTIMER_URL_PATH) == 'test123'

    def test_get_default_value(self):
        """
        GIVEN a prop is not set in the app config
        WHEN trying to get the prop by a key
        THEN return the default prop
        """
        app = Flask(__name__)
        assert get_by_key(app, URLTIMER_URL_PATH) == defaults[URLTIMER_URL_PATH]

    def test_exception(self):
        """
        GIVEN a prop is not set in the app config and has no the default value
        WHEN trying to get the prop by a key
        THEN raise AttributeError exception
        """
        app = Flask(__name__)
        key = 'this_does_not_exist'

        with pytest.raises(AttributeError) as e:
            get_by_key(app, key)

        assert e.match(f'The config is neither set or has value by this key: {key}')

