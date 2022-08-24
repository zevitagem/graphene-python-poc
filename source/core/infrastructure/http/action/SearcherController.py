from core.infrastructure.http.action.BaseController import BaseController
from core.application.services.Processor import Processor

class SearcherController(BaseController):

    resource_prefix = 'search'

    def __init__(self):
        self.service = Processor()

    def index(self):
        return BaseController.view(self, 'index', {
            "content": 'José'
        })

    def query(self, request):
        text = request['query']['name'] if ('name' in request['query']) else 'guest'

        query_string = '{ hello(name:"%s") }' % text
        result = self.service.execute(query_string)

        return BaseController.view(self, 'specific', {
            "content": result
        })

    def mutation(self, request):
        text = request['query']['name'] if ('name' in request['query']) else 'guest'

        mutation_string = '''
            mutation myFirstMutation {
                createPerson(name:"%s") {
                    ok
                    person {
                        name
                    }
                }
            }
        ''' % text

        result = self.service.execute(mutation_string)

        return BaseController.view(self, 'specific', {
            "content": result
        })
        