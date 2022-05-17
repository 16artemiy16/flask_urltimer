import json
from . import Storage
from ..log import log


class TxtStorage(Storage):
    """
    TxtStorage is used to import/export data to/from txt file.
    Each item will be placed in a separate line and represents a JSON object.
    """
    def export(self, data):
        filename = 'timings.txt'
        filepath = f'{self.app.root_path}/{filename}'

        with open(filepath, 'a') as f:
            data_str = json.dumps(data)
            f.write(f'{data_str}\n')

    def importt(self):
        filename = 'timings.txt'
        filepath = f'{self.app.root_path}/{filename}'

        data = []

        with open(filepath, 'r') as f:
            for line in f:
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError:
                    log.debug(f'TxtStorage failed to decode JSON from line {line}')
                    pass

        return data
