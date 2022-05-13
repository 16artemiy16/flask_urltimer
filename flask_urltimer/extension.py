import logging
from datetime import datetime
from flask import request

from .helpers import add_timemark, map_timemarks, get_timemarks
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
            add_timemark('start')

        @app.after_request
        def do_after(res):
            add_timemark('end')

            data = dict(
                timestamp=datetime.timestamp(datetime.now()),
                req=dict(
                    url=request.url
                ),
                timemarks=map_timemarks(get_timemarks())
            )
            TxtExporter(self.app, data).export()
            return res

