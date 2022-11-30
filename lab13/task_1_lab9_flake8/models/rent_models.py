from dataclasses import dataclass, field, asdict

from models.car_models import Car
from models.client_models import Client
from datetime import date, timedelta

from utils.helpers import CheckRent


@dataclass
class Rent:
    client_info: Client = field(repr=False)
    car_info: Car = field(repr=False)
    amount_of_days: int = 1
    rent_start_date: date = field(default=date.today())
    rent_end_date: date = field(init=False)
    renting_price: float = field(init=False)
    is_rent_over: bool = field(init=False, default=CheckRent())

    def __post_init__(self) -> None:
        self.renting_price = self.car_info.price_per_day * self.amount_of_days
        self.rent_end_date = self.rent_start_date + timedelta(
            days=self.amount_of_days)

    def __eq__(self, other):
        return self.renting_price == other.renting_price

    def __add__(self, other):
        return self.rent_end_date + timedelta(days=other)

    def __copy__(self):
        cls = self.__class__
        new_copy = cls.__new__(cls)
        new_copy.__dict__.update(asdict(self))
        return new_copy
