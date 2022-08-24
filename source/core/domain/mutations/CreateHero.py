from graphene import String, Mutation,  Int
from core.domain.interfaces.Character import Character

from core.infrastructure.repositories.DeveloperRepository import DeveloperRepository
from core.infrastructure.repositories.DroidRepository import DroidRepository


class CreateHero(Mutation):

    class Arguments:
        id = Int()
        name = String()
        type = String()
        company = String(required=False)
        hability = String(required=False)

    Output = Character

    def mutate(root, info, id, name, type, company=None, hability=None):
        if DroidRepository.isDroid(type):
            entity = DroidRepository.create(id, name, hability)
        else:
            entity = DeveloperRepository.create(id, name, company)

        return entity
