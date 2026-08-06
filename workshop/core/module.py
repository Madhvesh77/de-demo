from abc import ABC, abstractmethod


class WorkshopModule(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stage(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def status(self):
        return "READY"

    def reset(self):
        pass