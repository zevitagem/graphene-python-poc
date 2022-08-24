from graphene import String, Boolean, Field, Mutation
from core.domain.entities.Person import Person

class CreatePerson(Mutation):
    class Arguments:
        name = String()

    ok = Boolean()
    person = Field(lambda: Person)

    def mutate(root, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)
