import graphene
from graphene import ObjectType, String

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()
