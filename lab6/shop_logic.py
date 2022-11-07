class Brand:
    def __init__(self, name: str, country: str) -> None:
        self.name = name
        self.country = country

    def __str__(self):
        return f'Brand name - {self.name}\nBrand country - {self.country}\n'


class Model:
    brand_info: Brand

    def __init__(self, name: str, technical_description: str, brand: Brand) -> None:
        self.name = name
        self.technical_description = technical_description
        Model.brand_info = brand

    @classmethod
    def return_model_brand_info(cls):
        print("Information about the Model's Brand:")
        return cls.brand_info

    def __str__(self):
        return f'Model name - {self.name}\nModel description - {self.technical_description}\n'


brand1 = Brand('Tesla', 'USA')
model1 = Model('Model X', 'Electric Car', brand1)

print(model1.return_model_brand_info())


class Car:
    model_info: Model

    def __init__(self, plate_numbers: str, color: str, model: Model) -> None:
        self.plate_numbers = plate_numbers
        self.color = color
        Car.model_info = model

    @classmethod
    def return_car_model_info(cls):
        print("Information about the Cars's Model:")
        return cls.model_info


car1 = Car('1A24', 'Red', model1)
print(car1.return_car_model_info())


class Client:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f'{self.first_name} {self.last_name}'

    def __str__(self):
        print(f'First name - {self.first_name}\nLast name - {self.last_name}\nFull name - {self.first_name}\n')


class Rent:
    client_info: Client
    car_info: Car

    def __init__(self, price: float, client: Client, car: Car) -> None:
        self.price = price
        Rent.car_info = car
        Rent.client_info = client
