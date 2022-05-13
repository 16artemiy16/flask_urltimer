from abc import ABC, abstractmethod
import json


class Exporter(ABC):
    def __init__(self, app, data):
        self.app = app
        self.data = data

    @abstractmethod
    def export(self):
        pass


class TxtExporter(Exporter):
    def export(self):
        filename = 'timings.txt'
        filepath = f'{self.app.root_path}/{filename}'

        with open(filepath, 'a') as f:
            data_str = json.dumps([self.data])
            f.write(f'{data_str}\n')
