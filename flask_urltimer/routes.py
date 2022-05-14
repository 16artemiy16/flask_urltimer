from flask import Blueprint, render_template, request
from datetime import datetime

from .helpers import add_timemark, map_timemarks, get_timemarks
from .exporters import TxtExporter

bp = Blueprint(name='flask_urltimer', import_name=__name__, template_folder='templates')


@bp.get('/timings')
def render_timings_ui():
    return render_template('timings-ui.html')


def register(app):
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
        TxtExporter(app, data).export()
        return res

    app.register_blueprint(bp)
