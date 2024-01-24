from src.authorizer import Authorizer
from src.unauthorized_access_exception import UnauthorizedAccessException


class SafeCalculator:
    def __init__(self, authorizer: Authorizer):
        self.authorizer = authorizer

    def add(self, a, b) -> int:
        authorized = self.authorizer.authorize()

        # Bug! Should be `if not authorized`
        if authorized:
            raise UnauthorizedAccessException("Not authorized")
        return a + b
