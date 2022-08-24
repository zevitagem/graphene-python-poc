from graphene import ObjectType, String, Boolean


class Language(ObjectType):
    description = String(required=True)
    native = Boolean(required=True)
