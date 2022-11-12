from abc import ABC, abstractmethod


class ShopPresentLogic(ABC):

    @abstractmethod
    def get_dict_info(self) -> dict:
        raise NotImplemented

