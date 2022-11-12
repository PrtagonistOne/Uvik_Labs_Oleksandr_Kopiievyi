from dataclasses import dataclass, field

from models import pretty
from models_template.client_logic_blueprints import ClientLogic


@dataclass
class Client(ClientLogic):
    first_name: str
    last_name: str
    password: str = "Input you password."
    full_name: str = field(init=False)
    hashed_password: int = field(init=False)

    def __post_init__(self) -> None:
        self.full_name = f'{self.first_name} {self.last_name}'
        self.hashed_password = hash(self.password)
        del self.password

    def get_login_session_access(self, password: str) -> bool:
        if hash(password) == self.hashed_password:
            print("Access Granted!")
            return True
        print('Wrong Password')
        return False

    def get_client_info(self) -> str:
        print('CLIENTS PERSONAL INFO:')
        return pretty(self.__dict__)


if __name__ == "__main__":
    client1 = Client(first_name='John', last_name='Johnson', password='Secret')

    client_password = 'secret'
    if client1.get_login_session_access(password=client_password):
        print(client1.get_client_info())

    client_password = 'Secret'
    if client1.get_login_session_access(password=client_password):
        print(client1.get_client_info())



