import logging
from datetime import datetime
from timeit import default_timer as timer
from flask import g, request

from .exporters import TxtExporter

log = logging.getLogger('flask_urltimer')


class FlaskUrltimer(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        log.debug('init_app')

        @app.before_request
        def do_before():
            g.__flask_urltimer_timer_start = timer()

        @app.after_request
        def do_after(res):
            time = timer() - g.__flask_urltimer_timer_start
            data = dict(
                timestamp=datetime.timestamp(datetime.now()),
                req=dict(
                    url=request.url
                ),
                points=dict(
                    end=time
                )
            )
            TxtExporter(self.app, data).export()
            return res

