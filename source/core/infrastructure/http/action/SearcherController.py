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

    def __end(self, graphQL_string):
        result = self.service.execute(graphQL_string)
        #result = json.dumps(result.data, indent=4)

        return BaseController.view(self, 'specific', {
            "content": result
        })

    def list(self, request):
        query_string = '''
        {
            heroes {
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
        '''

        return self.__end(query_string)

    def query(self, request):
        id = request['query']['id'] if ('id' in request['query']) else None
        map = 'heroes' if id is None else 'hero'

        if map == 'heroes':
            return self.list(request)

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

        return self.__end(query_string)

    def mutation(self, request):
        type = request['query']['type']
        name = request['query']['name']
        company = request['query']['company'] if 'company' in request['query'] else None
        hability = request['query']['hability'] if 'hability' in request['query'] else None

        mutation_string = '''
            mutation myFirstMutation {
                CreateHero(type:"%s", name:"%s", company:"%s", hability:"%s") {
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
        ''' % (type, name, company, hability)

        return self.__end(mutation_string)
