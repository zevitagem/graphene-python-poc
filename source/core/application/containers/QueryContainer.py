from graphene import ObjectType, String

class QueryContainer(ObjectType):

    hello = String(name=String(default_value="guest"))
    goodbye = String()

    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'