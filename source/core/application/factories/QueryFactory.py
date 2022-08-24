from core.application.containers.QueryContainer import QueryContainer


class QueryFactory():

    @staticmethod
    def handle():
        return QueryFactory.__default()

    @staticmethod
    def __default():
        return QueryContainer
