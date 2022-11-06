class Brand:
    def __init__(self, name: str, country: str) -> None:
        self.name = name
        self.country = country


class Model:
    brand_info: Brand

    def __init__(self, name: str, technical_description: str, brand: Brand) -> None:
        self.name = name
        self.technical_description = technical_description
        Model.brand_info = brand


class Car:
    model_info: Model

    def __init__(self, plate_numbers: str, color: str, model: Model) -> None:
        self.plate_numbers = plate_numbers
        self.color = color
        Car.model_info = model


class Client:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f'{self.first_name} {self.last_name}'


class Rent:
    client_info: Client
    car_info: Car

    def __init__(self, price: float, client: Client, car: Car) -> None:
        self.price = price
        Rent.car_info = car
        Rent.client_info = client
