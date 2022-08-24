from graphene import Interface, ID, String, List
from core.domain.types.Language import Language
#from core.domain.types.Type import Type
from core.infrastructure.repositories.DroidRepository import DroidRepository


class Character(Interface):
    id = ID(required=True)
    name = String(required=True)
    languages = List(Language)

    #type = graphene.Field(Type)
    type = String(required=True)

    @classmethod
    def resolve_type(cls, instance, info):
        from core.domain.types.Droid import Droid
        from core.domain.types.Developer import Developer

        if DroidRepository.isDroid(instance.type):
            return Droid
        return Developer
