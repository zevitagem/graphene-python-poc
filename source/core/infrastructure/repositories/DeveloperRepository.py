from core.domain.entities.Developer import Developer
from .BaseRepository import BaseRepository


class DeveloperRepository(BaseRepository):

    mock_entities = {
        11: Developer(4, 'Dev: one', 'nanicas', 'php'),
        12: Developer(5, 'Dev: two', 'apple', 'javascript'),
        13: Developer(6, 'Dev: three', 'police', 'python')
    }

    @staticmethod
    def create(id, name, company, languages=['golang']):
        return Developer(id, name, company, languages[0])

    @staticmethod
    def isDeveloper(id):
        return id > 10
