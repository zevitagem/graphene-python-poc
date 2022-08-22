from core.infrastructure.http.action.BaseController import BaseController

class SearcherController(BaseController):

    resource_prefix = 'search'

    def index(self):
        return BaseController.view(self, 'index', {
            "content": 'José'
        })

    def specific(self):
        return BaseController.view(self, 'specific', {
            "content": 'José dog'
        })
        