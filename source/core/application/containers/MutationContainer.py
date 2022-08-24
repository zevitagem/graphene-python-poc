from graphene import ObjectType
from core.domain.mutations.CreatePerson import CreatePerson

class MutationContainer(ObjectType):
    create_person = CreatePerson.Field()