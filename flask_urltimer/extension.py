import logging

log = logging.getLogger('flask_urltimer')


class FlaskUrltimer(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        log.debug('init_app')
        app.teardown_appcontext(self.teardown)

    def teardown(self):
        log.debug('teardown')
