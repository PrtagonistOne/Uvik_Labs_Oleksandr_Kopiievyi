from abc import ABC, abstractmethod


class CarLogic(ABC):

    @abstractmethod
    def return_basic_info(self) -> str:
        raise NotImplemented

