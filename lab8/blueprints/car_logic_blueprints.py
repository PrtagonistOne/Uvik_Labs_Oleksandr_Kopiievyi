from abc import ABC, abstractmethod

from blueprints.shop_blueprint import ShopPresentLogic


class CarLogic(ShopPresentLogic):
    @abstractmethod
    def get_pretty_car_info(self) -> str:
        raise NotImplemented


class ModelLogic(ShopPresentLogic):
    @abstractmethod
    def get_pretty_model_info(self) -> str:
        raise NotImplemented


class BrandLogic(ShopPresentLogic):
    @abstractmethod
    def get_pretty_brand_info(self) -> str:
        raise NotImplemented
