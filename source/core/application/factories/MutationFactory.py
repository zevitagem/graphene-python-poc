from core.application.containers.MutationContainer import MutationContainer


class MutationFactory():

    @staticmethod
    def handle():
        return MutationFactory.__default()

    @staticmethod
    def __default():
        return MutationContainer
