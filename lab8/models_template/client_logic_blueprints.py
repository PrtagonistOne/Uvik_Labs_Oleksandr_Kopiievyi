from abc import ABC, abstractmethod


class ClientLogic(ABC):

    @abstractmethod
    def get_login_session_access(self, password: str) -> bool:
        raise NotImplemented

    @abstractmethod
    def get_client_info(self) -> bool:
        raise NotImplemented
