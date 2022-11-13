from models.car_models import Brand, Model, Car


def get_car_catalog_info(catalog_directory: tuple) -> None:
    catalog_top_intends = '______________________________CATALOG OF CARS______________________________'
    catalog_bottom_intends = f"{len(catalog_top_intends) * '_'}"

    print(catalog_top_intends)
    for car in catalog_directory:
        car.get_pretty_car_info()  # catalog content
    print(catalog_bottom_intends)


def get_dummy_brands() -> tuple:
    brand1 = Brand(name='Tesla', country='USA')
    brand2 = Brand(name='Toyota', country='Japan')
    return brand1, brand2


def get_dummy_models(brands: tuple) -> tuple:
    brand1, brand2 = brands
    model1 = Model(name='X', technical_description='Electric Car', brand_info=brand1)
    model2 = Model(name='3', technical_description='Electric Car', brand_info=brand1)
    model3 = Model(name='Camry', technical_description='Diesel', brand_info=brand2)
    model4 = Model(name='Corolla', technical_description='Gasoline', brand_info=brand2)
    return model1, model2, model3, model4


def get_dummy_cars(models: tuple) -> tuple:
    model1, model2, model3, model4 = models
    car1 = Car('1A24', 'Red', model1)
    car2 = Car('MDE2', 'Blue', model2)
    car3 = Car('DF32', 'Red', model3)
    car4 = Car('VD42', 'Green', model4)
    return car1, car2, car3, car4
