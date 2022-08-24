from core.domain.entities.Droid import Droid
from .BaseRepository import BaseRepository
from core.domain.types.Type import Type


class DroidRepository(BaseRepository):

    mock_entities = {
        1: Droid(1, 'Droid: one', 'eat', 'droid_language'),
        2: Droid(2, 'Droid: two', 'sleep', 'droid_language'),
        3: Droid(3, 'Droid: three', 'kill', 'droid_language')
    }

    @staticmethod
    def create(id, name, hability, languages=['droid_language']):
        return Droid(id, name, hability, languages[0])

    @staticmethod
    def isDroid(type):
        return type == Type.DROID.value
