from core.domain.graphene.Query import Query as GrapheneQuery
from graphene import Schema

class SchemaFactory():
    
    def handle(self):
        query = self.__graphene()
        return Schema(query=query)

    def __graphene(self):
        return GrapheneQuery