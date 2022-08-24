from graphene import ObjectType, String
from core.domain.interfaces.Character import Character

class Droid(ObjectType):

    class Meta:
        interfaces = (Character, )

    hability = String(required=True)
