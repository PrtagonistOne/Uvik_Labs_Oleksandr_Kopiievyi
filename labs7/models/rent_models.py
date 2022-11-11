from dataclasses import dataclass, field
from .car_models import Car, Brand, Model
from .client_models import Client


@dataclass
class Rent:
    client_info: Client = field(repr=False)
    car_info: Car = field(repr=False)
    amount_of_days: int = 1
    renting_price: float = field(init=False)

    def __post_init__(self):
        self.renting_price = self.car_info.price_per_day * self.amount_of_days


if __name__ == "__main__":
    brand1 = Brand(name='Tesla', country='USA')
    model1 = Model(name='X', technical_description='Electric Car', brand_info=brand1)
    car1 = Car('1A24', 'Red', model1)
    client1 = Client(first_name='John', last_name='Johnson', password='Secret')

    rent1 = Rent(client_info=client1, car_info=car1, amount_of_days=3)

    print(rent1)
