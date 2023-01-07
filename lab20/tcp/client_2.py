from tcp.client import start_client_connection
from tcp.utils.user import User

if __name__ == "__main__":
    user2 = User(username='MagnusCarlsen420', message='Hello, everybody!')
    start_client_connection(user=user2)