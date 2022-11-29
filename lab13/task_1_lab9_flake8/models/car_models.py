from dataclasses import dataclass


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


@dataclass
class Car:
    plate_numbers: str
    color: str
    model_info: Model
    price_per_day: float = 100.0


if __name__ == "__main__":
    brand1 = Brand(name='Tesla', country='USA')
    print(brand1)

    model1 = Model(name='X',
                   technical_description='Electric Car',
                   brand_info=brand1)

    print(model1)
    car1 = Car('1A24', 'Red', model1)
    # print(car1)
