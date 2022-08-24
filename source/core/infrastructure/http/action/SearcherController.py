from core.infrastructure.http.action.BaseController import BaseController
from core.application.services.Processor import Processor
#import json


class SearcherController(BaseController):

    resource_prefix = 'search'

    def __init__(self):
        self.service = Processor()

    def index(self, args):
        return BaseController.view(self, 'index', {
            "content": 'Hello World, José!'
        })

    def query(self, request):
        id = request['query']['id'] if ('id' in request['query']) else 1

        query_string = '''
        {
            hero(id: %s) {
                id
                name
                type
                languages {
                    description
                    native
                }
                ... on Droid {
                    hability
                }
                ... on Developer {
                    company
                }
            }
        }
        ''' % id

        result = self.service.execute(query_string)
        #result = json.dumps(result.data, indent=4)

        return BaseController.view(self, 'specific', {
            "content": result
        })

    def mutation(self, request):
        id = request['query']['id']
        type = request['query']['type']
        name = request['query']['name']
        company = request['query']['company'] if 'company' in request['query'] else None
        hability = request['query']['hability'] if 'hability' in request['query'] else None

        mutation_string = '''
            mutation myFirstMutation {
                CreateHero(id:%s, type:"%s", name:"%s", company:"%s", hability:"%s") {
                    id
                    name
                    type
                    languages {
                        description
                    }
                    languages {
                        description
                        native
                    }
                    ... on Droid {
                        hability
                    }
                    ... on Developer {
                        company
                    }
                }
            }
        ''' % (id, type, name, company, hability)

        result = self.service.execute(mutation_string)

        return BaseController.view(self, 'specific', {
            "content": result
        })
