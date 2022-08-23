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

        query_string = '{ hello(name:"(%s)") }' % text
        result = self.service.execute(query_string)

        return BaseController.view(self, 'specific', {
            "content": result
        })
        