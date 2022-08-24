from core.application.factories import * 

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
            "query": query
        })

    def execute(self, arg):
        return self.schema.execute(arg)