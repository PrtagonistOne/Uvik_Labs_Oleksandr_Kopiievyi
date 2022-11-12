from typing import Generator

from models.car_models import Car, Brand, Model
from models.client_models import Client
from models.rent_models import Rent


def get_car_catalog_info(catalog_directory: Generator) -> None:
    catalog_top_intends = '______________________________CATALOG OF CARS______________________________'
    catalog_top_intends = f"{len(catalog_top_intends) * '_'}"

    print(catalog_top_intends)
    [print(car.return_basic_info(), '\n') for car in catalog_directory]  # catalog content
    print(catalog_top_intends)


# User Story
# Client Walks into a Car Rent Shop
# Available brands
brand1 = Brand(name='Tesla', country='USA')
brand2 = Brand(name='Toyota', country='Japa')
# Available Models
model1 = Model(name='X', technical_description='Electric Car', brand_info=brand1)
model2 = Model(name='3', technical_description='Electric Car', brand_info=brand1)
model3 = Model(name='Camry', technical_description='Diesel', brand_info=brand2)
model4 = Model(name='Corolla', technical_description='Gasoline', brand_info=brand2)
# Available Cars
current_cars_amount = 4
car1 = Car('1A24', 'Red', model1)
car2 = Car('MDE2', 'Blue', model2)
car3 = Car('DF32', 'Red', model3)
car4 = Car('VD42', 'Green', model4)
car_catalog = (eval(f"car{i}") for i in range(1, current_cars_amount + 1))
# Client observes the catalog
get_car_catalog_info(car_catalog)

# Client fills out registration form at the reception desk
# And the receptionist input the data into the database
client1 = Client(first_name='John', last_name='Johnson', password='Secret')
print(client1.get_client_info(), '\n')

# Client is renting a car using his password (not successful)
if not client1.get_login_session_access('secret'):
    print('Try again', '\n')
# Client remembers corrects the password and started filling out a rent form online (not successful)
if client1.get_login_session_access('Secret'):
    rent1 = Rent(client_info=client1, car_info=car1, amount_of_days=3)
    # Client seems following message
    print(f'You obligated to pay - {rent1.renting_price} for {rent1.amount_of_days} days.')
    # Client remembered that he had no money and leaves the store sad :(
