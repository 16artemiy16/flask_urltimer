from timeit import default_timer as timer
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
