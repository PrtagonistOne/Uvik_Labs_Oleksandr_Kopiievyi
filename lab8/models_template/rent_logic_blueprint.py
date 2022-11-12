from abc import ABC, abstractmethod


class RentLogic(ABC):

    @abstractmethod
    def is_rent_over(self) -> str:
        raise NotImplemented

