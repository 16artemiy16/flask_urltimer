import json
from . import Exporter


class TxtExporter(Exporter):
    """
    TxtExporter is used to export data to txt file.
    Each item will be placed in a separate line and represents a JSON object.
    """
    def export(self):
        filename = 'timings.txt'
        filepath = f'{self.app.root_path}/{filename}'

        with open(filepath, 'a') as f:
            data_str = json.dumps(self.data)
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
                    pass

        return data
