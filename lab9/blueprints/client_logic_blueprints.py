from abc import abstractmethod


class ClientLogic:

    @abstractmethod
    def get_login_session_access(self, password: str) -> bool:
        pass

    @abstractmethod
    def _get_hashed_password(self) -> None:
        pass
