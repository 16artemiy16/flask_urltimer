import uuid
from flask import g
from time import time
from timeit import default_timer as timer

_TIMEMARK_BUILDER_KEY = 'urltimer_builder'


def init_timememark_builder():
    setattr(g, _TIMEMARK_BUILDER_KEY, TimemarkBuilder())


def get_timemark_builder():
    return getattr(g, _TIMEMARK_BUILDER_KEY)


class TimemarkBuilder:
    def __init__(self):
        self.data = dict(
            id=uuid.uuid4().hex,
            timestamp=int(time()*1000),
            req=dict(),
            timemarks=dict(),
            source=dict(
                lines=None,
                linenum=None
            ),
            duration=None,
        )

    def set_req_url(self, v):
        self.data['req']['url'] = v
        return self

    def set_source(self, v):
        self.data['source'] = v
        return self

    def add_timemark(self, name, line=None):
        self.data['timemarks'][name] = [timer(), line]

    def build(self):
        return dict(
            id=self.data['id'],
            timestamp=self.data['timestamp'],
            req=self.data['req'],
            timemarks=self._map_timemarks(),
            source=self.data['source'],
            duration=round(self.data['timemarks']['end'][0] - self.data['timemarks']['start'][0], 4)
        )

    def _map_timemarks(self):
        timemarks = self.data['timemarks']
        start = timemarks['start'][0]
        results = {}
        for key, value in timemarks.items():
            line = value[1]
            duration = value[0] - start if key != 'start' else 0
            results[key] = [duration, line]
        return results
