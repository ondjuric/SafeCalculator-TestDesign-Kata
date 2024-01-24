from src.authorizer import Authorizer


class AlwaysAuthorized(Authorizer):
    def authorize(self) -> bool:
        # Simple authorization logic, for example, always authorize
        return True
