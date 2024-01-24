from src.authorizer import Authorizer
from src.unauthorized_access_exception import UnauthorizedAccessException


class SafeCalculator:
    def __init__(self, authorizer: Authorizer):
        self.authorizer = authorizer

    def add(self, a, b) -> int:
        authorized = self.authorizer.authorize()

        return self.add_with_authorization_check(a, b, authorized)

    @staticmethod
    def add_with_authorization_check(a, b, authorized=None) -> int:
        # Bug! Should be `if not authorized`
        if not authorized:
            raise UnauthorizedAccessException("Not authorized")
        return a + b
