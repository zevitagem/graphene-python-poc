from graphene import ObjectType, Field, Int, List
from core.domain.interfaces.Character import Character

from core.infrastructure.repositories.DeveloperRepository import DeveloperRepository
from core.infrastructure.repositories.DroidRepository import DroidRepository


class QueryContainer(ObjectType):

    hero = Field(
        Character,
        required=True,
        id=Int(required=False)
    )

    heroes = Field(
        List(Character),
        required=True
    )

    def resolve_hero(root, info, id):
        if DeveloperRepository.isDeveloper(id):
            return DeveloperRepository().find(id)
        return DroidRepository().find(id)
