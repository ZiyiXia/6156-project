from abc import ABC, abstractmethod


class BaseApplicationExcetion:

    def __init__(self):
        pass


class BaseApplicationResource(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_links(self, resource_data):
        pass
