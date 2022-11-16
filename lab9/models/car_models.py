from dataclasses import dataclass, asdict

from utils.helpers import prettify


@dataclass
class Brand:
    """Model for Brand of the car"""
    name: str
    country: str

    def __repr__(self) -> dict:
        return asdict(self)

    def __str__(self) -> None:
        print('General Brand info:')
        return prettify(self.__repr__())


@dataclass
class Model:
    name: str
    technical_description: str
    brand_info: Brand

    def __repr__(self) -> dict:
        return asdict(self)

    def __str__(self) -> None:
        print(f"Brand info about the MODEL[{self.name}]:")
        return prettify(self.brand_info.__repr__())


@dataclass
class Car:
    plate_numbers: str
    color: str
    model_info: Model
    price_per_day: float = 100.0

    def __repr__(self) -> dict:
        return asdict(self)

    def __str__(self) -> None:
        print(f"Model info about the "
              f"CAR[{self.plate_numbers}],"
              f" COLOR[{self.color}], "
              f"DEFAULT PRICING PER DAY[{self.price_per_day}]:")
        return prettify(self.model_info.__repr__())


if __name__ == "__main__":
    brand1 = Brand(name='Tesla', country='USA')
    print(brand1)

    model1 = Model(name='X', technical_description='Electric Car', brand_info=brand1)

    print(model1)
    car1 = Car('1A24', 'Red', model1)
    print(car1)

