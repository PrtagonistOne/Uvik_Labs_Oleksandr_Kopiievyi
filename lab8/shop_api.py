import sys
import time
from getpass import getpass

from models.car_models import Car, Brand, Model
from models.client_models import Client
from models.rent_models import Rent


def get_car_catalog_info(catalog_directory: tuple):
    catalog_top_intends = '______________________________CATALOG OF CARS______________________________'
    catalog_bottom_intends = f"{len(catalog_top_intends) * '_'}"

    print(catalog_top_intends)
    for car in catalog_directory:
        car.get_pretty_car_info()  # catalog content
    print(catalog_bottom_intends)


def perform_user_action(client: Client, car: Car, days: int) -> None:
    while True:
        client_password = getpass("Enter the Password: ", stream=sys.stderr)
        if client.get_login_session_access(password=client_password):
            print('Access granted!')
            rent1 = Rent(client_info=client, car_info=car, amount_of_days=days)
            rent1.get_pretty_rent_info()
            print(f'You obligated to pay - {rent1.renting_price} for {rent1.amount_of_days} days.')
            # Client remembered that he had no money and leaves the store sad :(
        else:
            print('Access Denied!')
        user_input = input('Wish to access again? (Y/N)').lower()
        if user_input == 'y':
            continue
        elif user_input == 'n':
            break


# User Story
# Client Walks into a Car Rent Shop
# Available brands
brand1 = Brand(name='Tesla', country='USA')
brand2 = Brand(name='Toyota', country='Japan')
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
car_catalog = (car1, car2, car3, car4)
# Client observes the catalog
get_car_catalog_info(car_catalog)

# Client fills out registration form at the reception desk
# And the receptionist input the data into the database
client1 = Client(first_name='John', last_name='Johnson', password='Secret')
client1.get_pretty_client_info()
time.sleep(0.3)
# Client is renting a chosen car with chosen day using his password
days_to_rent = 3
perform_user_action(client=client1, car=car1, days=days_to_rent)
