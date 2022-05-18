from timeit import default_timer as timer
import inspect
from flask import g

_TIMEMARKS_ATTR = '__flask_urltimer_timer'


def get_timemarks():
    return getattr(g, _TIMEMARKS_ATTR,  {})


def add_timemark(name):
    marks = get_timemarks()
    marks[name] = timer()
    setattr(g, _TIMEMARKS_ATTR, marks)


def map_timemarks(timemarks):
    start = timemarks['start']
    results = {}

    for key, value in timemarks.items():
        results[key] = value - start if key != 'start' else 0

    return results



_FN_SOURCE_ATTR = '__flask_urltimer_fnsource'


def check_source(fn):
    def inner(*args, **kwargs):
        setattr(g, _FN_SOURCE_ATTR, inspect.getsource(fn))
        return fn(*args, **kwargs)

    return inner


def get_checked_source():
    return getattr(g, _FN_SOURCE_ATTR, None)
