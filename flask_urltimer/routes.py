from flask import Blueprint, render_template, request
from time import time
import atexit
import uuid

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


def register(app):
    ui_url = configer.get_by_key(app, configer.URLTIMER_URL_PATH)

    @bp.get(f'/{ui_url}')
    def render_ui():
        return render_template('timings/index.html')

    @bp.get('/timings/api/items')
    def get_items():
        def add_total_duration(item):
            item['duration'] = round(item['timemarks']['end'][0] - item['timemarks']['start'][0], 4)
            return item

        data = storage.importt(app)

        data = [add_total_duration(i) for i in data]
        res = dict(items=data)
        return res

    @app.before_request
    def do_before():
        add_timemark('start')

    @app.after_request
    def do_after(res):
        if not get_checked_source():
            return res

        add_timemark('end')
        data = dict(
            id=uuid.uuid4().hex,
            timestamp=int(time()*1000),
            req=dict(
                url=request.url
            ),
            timemarks=map_timemarks(get_timemarks()),
            source=get_checked_source()
        )
        storage.export(app, data)
        return res

    app.register_blueprint(bp)

    @atexit.register
    def cleanup():
        if configer.get_by_key(app, configer.URLTIMER_CLEANUP_ON_SHUTDOWN):
            storage.cleanup(app)
