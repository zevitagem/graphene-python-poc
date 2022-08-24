from graphene import ObjectType, String
from core.domain.interfaces.Character import Character


class Developer(ObjectType):

    class Meta:
        interfaces = (Character, )

    company = String(required=True)
