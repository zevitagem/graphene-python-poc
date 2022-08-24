from graphene import ObjectType
from core.domain.mutations.CreateHero import CreateHero


class MutationContainer(ObjectType):

    CreateHero = CreateHero.Field()
