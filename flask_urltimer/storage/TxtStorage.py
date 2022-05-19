import json
import os
from . import Storage
from ..log import log


class TxtStorage(Storage):
    """
    TxtStorage is used to import/export data to/from txt file.
    Each item will be placed in a separate line and represents a JSON object.
    """

    @property
    def _filepath(self):
        filename = 'timings.txt'
        return f'{self.app.root_path}/{filename}'

    def export(self, data):
        with open(self._filepath, 'a') as f:
            data_str = json.dumps(data)
            f.write(f'{data_str}\n')

    def importt(self):
        data = []
        try:
            with open(self._filepath, 'r') as f:
                for line in f:
                    try:
                        data.append(json.loads(line))
                    except json.JSONDecodeError:
                        log.debug(f'TxtStorage failed to decode JSON from line {line}')
                        pass
        except FileNotFoundError:
            log.debug(f'TxtStorage returning empty list as file is not found by path {self._filepath}')
            pass

        return data

    def cleanup(self):
        try:
            os.unlink(self._filepath)
            log.debug(f'TxtStorage cleanup succeed - removed {self._filepath}')
        except FileNotFoundError:
            log.debug(f'TxtStorage cleanup skipped - no file by path {self._filepath}')
