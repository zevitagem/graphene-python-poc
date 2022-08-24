from core.application.factories import *

from core.domain.types.Developer import Developer
from core.domain.types.Droid import Droid


class Processor():

    def modules(self):
        tup = (
            ('mutation', MutationFactory),
            ('query', QueryFactory),
            ('schema', SchemaFactory)
        )

        return dict((x, y) for x, y in tup)

    def __init__(self):
        modules = self.modules()

        mutation = modules['mutation'].MutationFactory.handle()
        query = modules['query'].QueryFactory.handle()

        self.schema = modules['schema'].SchemaFactory.handle({
            "mutation": mutation,
            "query": query,
            "types": [Developer, Droid]
        })

    def execute(self, arg):
        return self.schema.execute(arg)
