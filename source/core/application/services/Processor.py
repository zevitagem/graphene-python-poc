from core.application.factories.SchemaFactory import SchemaFactory

class Processor():
    
    def __init__(self):
        self.factory = SchemaFactory()
        self.schema = self.factory.handle()

    def execute(self, arg):
        return self.schema.execute(arg)