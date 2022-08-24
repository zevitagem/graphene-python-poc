from graphene import ObjectType, Field, Int, List
from core.domain.interfaces.Character import Character

from core.infrastructure.repositories.DeveloperRepository import DeveloperRepository
from core.infrastructure.repositories.DroidRepository import DroidRepository


class QueryContainer(ObjectType):

    __developer_repository_instance = DeveloperRepository()
    __droid_repository_instance = DroidRepository()

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
            return QueryContainer.__developer_repository_instance.find(id)
        return QueryContainer.__droid_repository_instance.find(id)

    def resolve_heroes(root, info):
        developers = [
            value for _, value in QueryContainer.__developer_repository_instance.list().items()]
        droids = [
            value for _, value in QueryContainer.__droid_repository_instance.list().items()]

        return developers + droids
