from abc import ABC, abstractmethod


class Storage(ABC):
    """ Base Storage class. """

    def __init__(self, app):
        self.app = app

    @abstractmethod
    def export(self, data):
        pass

    @abstractmethod
    def importt(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass
