from graphene import Schema

class SchemaFactory():

    @staticmethod
    def handle(config):

        if 'query' not in config and 'mutation' not in config:
            raise ValueError('The "query" or "mutation" attribute must be exists in config')

        return Schema(**config)