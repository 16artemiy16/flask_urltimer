from flask import Blueprint, render_template, request
from datetime import datetime

from . import configer
from .helpers import add_timemark, map_timemarks, get_timemarks, get_checked_source
from . import storage

bp = Blueprint(
    name='flask_urltimer',
    import_name=__name__,
    template_folder='templates',
    static_url_path='',
    static_folder="templates/timings",
)


@bp.get('/ui')
def render_ui():
    return render_template('timings/index.html')


def register(app):
    ui_url = configer.get_by_key(app, configer.URLTIMER_URL_PATH)

    @bp.get(f'/{ui_url}')
    def render_timings_ui():
        return render_template('timings-ui.html')

    @bp.get('/timings/api/items')
    def get_items():
        data = storage.importt(app)
        res = dict(items=data)
        return res

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
            timemarks=map_timemarks(get_timemarks()),
            source=get_checked_source()
        )
        storage.export(app, data)
        return res

    app.register_blueprint(bp)
