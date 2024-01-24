from src.authorizer import Authorizer


class NeverAuthorized(Authorizer):
    def authorize(self) -> bool:
        # Custom authorization logic, for example, based on user input or external service
        return False
