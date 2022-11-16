import time

from endpoints.car_endpoints import get_car_catalog_info, get_dummy_brands, get_dummy_models, get_dummy_cars
from endpoints.client_endpoints import get_client_rent_info, get_dummy_client_data

# User Story
# Client Walks into a Car Rent Shop
# Available brands
available_dummy_brands = get_dummy_brands()
# Available Models
available_dummy_models = get_dummy_models(available_dummy_brands)
# Available Cars
available_dummy_cars = get_dummy_cars(available_dummy_models)
# Client observes the catalog
get_car_catalog_info(available_dummy_cars)
# Client registered his account
dummy_client = get_dummy_client_data()
print(dummy_client)
time.sleep(0.2)
# Client is renting a chosen car with chosen day using his password
days_to_rent = 3
get_client_rent_info(client=dummy_client, car=available_dummy_cars[0], days=days_to_rent)
