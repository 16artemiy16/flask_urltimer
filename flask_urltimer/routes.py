from flask import Blueprint, render_template, request, g
import atexit

from . import configer
from .helpers import add_timemark, get_checked_source
from .timemark_builder import init_timememark_builder, get_timemark_builder
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
        data = storage.importt(app)
        res = dict(items=data)
        return res

    @app.before_request
    def do_before():
        init_timememark_builder()
        get_timemark_builder().add_timemark('start')
        add_timemark('start')

    @app.after_request
    def do_after(res):
        if not get_checked_source():
            return res

        add_timemark('end')
        get_timemark_builder().set_req_url(request.url)
        storage.export(app, get_timemark_builder().build())
        return res

    app.register_blueprint(bp)

    @atexit.register
    def cleanup():
        if configer.get_by_key(app, configer.URLTIMER_CLEANUP_ON_SHUTDOWN):
            storage.cleanup(app)
