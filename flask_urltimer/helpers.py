from timeit import default_timer as timer
import inspect
import sys
import traceback
from flask import g

_TIMEMARKS_ATTR = '__flask_urltimer_timer'


def get_timemarks():
    return getattr(g, _TIMEMARKS_ATTR,  {})


def find_line(find_filename, find_fn):
    for threadId, stack in sys._current_frames().items():
        for filename, lineno, name, line in traceback.extract_stack(stack):
            if filename == find_filename and name == find_fn:
                return lineno


def add_timemark(name):
    line = None
    if name != 'start' and name != 'end':
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        line = find_line(module.__file__, frame.function)
    marks = get_timemarks()
    marks[name] = [timer(), line]
    setattr(g, _TIMEMARKS_ATTR, marks)


def map_timemarks(timemarks):
    start = timemarks['start'][0]
    results = {}

    for key, value in timemarks.items():
        line = value[1]
        duration = value[0] - start if key != 'start' else 0
        results[key] = [duration, line]
    return results



_FN_SOURCE_ATTR = '__flask_urltimer_fnsource'


def check_source(fn):
    def inner(*args, **kwargs):
        lines, linenum = inspect.getsourcelines(fn)
        setattr(g, _FN_SOURCE_ATTR, dict(lines=lines, linenum=linenum))
        return fn(*args, **kwargs)

    inner.__name__ = fn.__name__

    return inner


def get_checked_source():
    return getattr(g, _FN_SOURCE_ATTR, None)
