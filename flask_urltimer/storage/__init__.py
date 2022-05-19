"""
Storages are used to import/export tracked data.
"""

from .Storage import *
from .TxtStorage import *

from .. import configer

_engine_str_cls_map = {
    'txt': TxtStorage,
}


def _get_storage_by_app(app):
    engine_str = configer.get_by_key(app, configer.URLTIMER_STORAGE_ENGINE)
    engine_cls = _engine_str_cls_map.get(engine_str, None)

    if engine_cls is None:
        raise TypeError(f'{engine_str} is an incorrect engine. Only {list(_engine_str_cls_map.keys())} are available.')

    return engine_cls(app)


def export(app, data):
    storage = _get_storage_by_app(app)
    storage.export(data)


def importt(app):
    storage = _get_storage_by_app(app)
    return storage.importt()


def cleanup(app):
    _get_storage_by_app(app).cleanup()

__all__ = [
    'export',
    'importt',
    'cleanup',
]
