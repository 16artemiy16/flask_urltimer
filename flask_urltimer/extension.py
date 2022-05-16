from . import routes
from .log import log


class FlaskUrltimer(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        log.debug('init_app')
        routes.register(app)
