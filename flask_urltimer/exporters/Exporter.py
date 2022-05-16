from abc import ABC, abstractmethod


class Exporter(ABC):
    """
    Base Exporter class. It's abstract export() is not implemented here.
    """

    def __init__(self, app, data):
        self.app = app
        self.data = data

    @abstractmethod
    def export(self):
        pass
