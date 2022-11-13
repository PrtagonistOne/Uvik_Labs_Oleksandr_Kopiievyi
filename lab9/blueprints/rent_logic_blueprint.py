from abc import abstractmethod

from blueprints.shop_blueprint import ShopPresentLogic


class RentLogic(ShopPresentLogic):

    @abstractmethod
    def get_pretty_rent_info(self) -> None:
        raise NotImplemented
