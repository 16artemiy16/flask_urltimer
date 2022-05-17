"""
Configer helps to get the config options via app.
"""

from .log import log

URLTIMER_URL_PATH = 'URLTIMER_URL_PATH'
URLTIMER_STORAGE_ENGINE = 'URLTIMER_STORAGE_ENGINE'

defaults = {
    URLTIMER_URL_PATH: 'timings-ui',
    URLTIMER_STORAGE_ENGINE: 'txt',
}


def get_by_key(app, key):
    set_value = app.config.get(key)
    default_value = defaults.get(key, None)

    if set_value is not None:
        log.debug(f'Config {key}={set_value} (from app config)')
        return set_value
    if default_value is not None:
        log.debug(f'Config {key}={default_value} (default, not set in app config)')
        return default_value

    raise AttributeError(f'The config is neither set or has value by this key: {key}')
