from abc import abstractmethod

from blueprints.shop_blueprint import ShopPresentLogic


class ClientLogic(ShopPresentLogic):

    @abstractmethod
    def get_login_session_access(self, password: str) -> bool:
        raise NotImplemented

    @abstractmethod
    def get_pretty_client_info(self) -> bool:
        raise NotImplemented

    @abstractmethod
    def _get_hashed_password(self) -> None:
        raise NotImplemented
