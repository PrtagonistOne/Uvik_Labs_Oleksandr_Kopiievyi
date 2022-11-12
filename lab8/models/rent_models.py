from dataclasses import dataclass, field, asdict

from models import prettify
from models.car_models import Car, Brand, Model
from models.client_models import Client
from datetime import date, timedelta

from blueprints.rent_logic_blueprint import RentLogic


@dataclass
class Rent(RentLogic):
    client_info: Client = field(repr=False)
    car_info: Car = field(repr=False)
    amount_of_days: int = 1
    rent_start_date: date = field(default=date.today())
    rent_end_date: date = field(init=False)
    renting_price: float = field(init=False)
    rent_over: bool = False

    def __post_init__(self) -> None:
        self.renting_price = self.car_info.price_per_day * self.amount_of_days
        self.rent_end_date = self.rent_start_date + timedelta(days=self.amount_of_days)

    def is_rent_over(self) -> bool:
        return self.rent_end_date.day - date.today().day == 0

    def get_dict_info(self) -> dict:
        return asdict(self)

    def get_pretty_rent_info(self) -> None:
        print('General rent info:')
        prettify(self.get_dict_info())

    def __eq__(self, other):
        return self.renting_price == other.renting_price

    def __add__(self, other):
        return self.rent_end_date + timedelta(days=other)

    def __copy__(self):
        cls = self.__class__
        new_copy = cls.__new__(cls)
        new_copy.__dict__.update(asdict(self))
        return new_copy


if __name__ == "__main__":
    brand1 = Brand(name='Tesla', country='USA')
    model1 = Model(name='X', technical_description='Electric Car', brand_info=brand1)
    car1 = Car('1A24', 'Red', model1)
    car2 = Car('FDA2', 'Blue', model1)

    client1 = Client(first_name='John', last_name='Johnson', password='Secret')
    client2 = Client(first_name='John', last_name='Wattson', password='Secret')

    rent1 = Rent(client_info=client1, car_info=car1, amount_of_days=3)
    rent2 = Rent(client_info=client2, car_info=car2, amount_of_days=3)

    print(f"Checking if rent is over - {rent1.is_rent_over()}")
    # two different clients renting comparison overloaded
    print(f"Comparing two different rent object {rent1 == rent2}")
    # adding certain days to the ending rent deadline
    print(f"Performing an arithmetic exercise - {rent1 + 4}")
    # copy of the rent
    rent_copy = rent1.__copy__()
    print('Checking if copy is good')
    print(rent_copy.client_info == rent1.client_info.get_dict_info())
    print(rent_copy.client_info is rent1.client_info.get_dict_info())
