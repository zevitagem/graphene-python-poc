from core.domain.entities.Language import Language
from core.domain.types.Type import Type


class Developer():

    def __init__(self, id, name, company, language):
        self.id = id
        self.name = name
        self.company = company
        self.type = Type.DEVELOPER.value
        self.languages = [
            Language(language, False)
        ]
