from models.car_models import Car
from models.client_models import Client
from models.rent_models import Rent
import sys
from getpass import getpass


def get_client_rent_info(client: Client, car: Car, days: int) -> None:
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


def get_dummy_client_data() -> Client:
    return Client(first_name='John', last_name='Johnson', password='Secret')
