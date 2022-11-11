from dataclasses import dataclass

from models import pretty


@dataclass
class Brand:
    """Model for Brand of the car"""
    name: str
    country: str


@dataclass
class Model:
    name: str
    technical_description: str
    brand_info: Brand

    def return_model_brand_info(self) -> str:
        print(f"Brand info about the MODEL[{self.name}]:")
        return pretty(self.brand_info.__dict__)


@dataclass
class Car:
    plate_numbers: str
    color: str
    model_info: Model
    price_per_day: float = 100.0

    def return_car_model_info(self) -> str:
        print(f"Model info about the "
              f"CAR[{self.plate_numbers}],"
              f" COLOR[{self.color}], "
              f"DEFAULT PRICING PER DAY[{self.price_per_day}]:")
        self.model_info.__dict__['brand_info'] = '\n' + pretty(self.model_info.__dict__['brand_info'].__dict__)
        return pretty(self.model_info.__dict__)


if __name__ == "__main__":
    brand1 = Brand(name='Tesla', country='USA')
    model1 = Model(name='X', technical_description='Electric Car', brand_info=brand1)

    print(model1.return_model_brand_info())

    car1 = Car('1A24', 'Red', model1)
    print(car1.return_car_model_info())
