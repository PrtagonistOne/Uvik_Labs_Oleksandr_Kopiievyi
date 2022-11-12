from dataclasses import dataclass, asdict

from models import prettify
from blueprints.car_logic_blueprints import CarLogic, ModelLogic, BrandLogic


@dataclass
class Brand(BrandLogic):
    """Model for Brand of the car"""
    name: str
    country: str

    def get_dict_info(self) -> dict:
        return asdict(self)

    def get_pretty_brand_info(self) -> None:
        print('General Brand info:')
        prettify(self.get_dict_info())


@dataclass
class Model(ModelLogic):
    name: str
    technical_description: str
    brand_info: Brand

    def get_dict_info(self) -> dict:
        return asdict(self)

    def get_pretty_model_info(self) -> None:
        print(f"Brand info about the MODEL[{self.name}]:")
        prettify(self.brand_info.get_dict_info())


@dataclass
class Car(CarLogic):
    plate_numbers: str
    color: str
    model_info: Model
    price_per_day: float = 100.0

    def get_dict_info(self) -> dict:
        return asdict(self)

    def get_pretty_car_info(self) -> None:
        print(f"Model info about the "
              f"CAR[{self.plate_numbers}],"
              f" COLOR[{self.color}], "
              f"DEFAULT PRICING PER DAY[{self.price_per_day}]:")
        prettify(self.model_info.get_dict_info())


if __name__ == "__main__":
    brand1 = Brand(name='Tesla', country='USA')
    brand1.get_pretty_brand_info()

    model1 = Model(name='X', technical_description='Electric Car', brand_info=brand1)

    model1.get_pretty_model_info()
    car1 = Car('1A24', 'Red', model1)
    car1.get_pretty_car_info()

