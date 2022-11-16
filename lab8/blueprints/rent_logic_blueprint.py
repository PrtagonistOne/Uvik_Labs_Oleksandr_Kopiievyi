from abc import abstractmethod


class RentLogic:

    @abstractmethod
    def is_rent_over(self) -> str:
        pass
