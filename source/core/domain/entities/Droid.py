from core.domain.entities.Language import Language
from core.domain.types.Type import Type


class Droid():

    def __init__(self, id, name, hability, language):
        self.id = id
        self.name = name
        self.hability = hability
        self.type = Type.DROID.value
        self.languages = [
            Language(language, True)
        ]
