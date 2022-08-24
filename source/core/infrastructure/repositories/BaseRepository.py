from abc import ABC, abstractmethod


class BaseRepository(ABC):

    def find(self, id):
        return self.mock_entities[id] if id in self.mock_entities else None

    def list(self):
        return self.mock_entities
