import sys
from dataclasses import dataclass, field
import os
import binascii
from getpass import getpass

from backports.pbkdf2 import pbkdf2_hmac

from models import prettify


@dataclass
class Client:
    first_name: str
    last_name: str
    password: str = field(repr=False)
    full_name: str = field(init=False)
    hashed_password: bytes = field(init=False)

    def __post_init__(self) -> None:
        self.full_name = f'{self.first_name} {self.last_name}'
        self._get_hashed_password()

    def _get_hashed_password(self):
        self.hashed_password = self.hash_password(self.password)
        setattr(self, 'password', '*****')

    @staticmethod
    def hash_password(password) -> bytes:
        salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
        key = pbkdf2_hmac("sha256", password.encode("utf8"), salt, 50000, 32)
        return binascii.hexlify(key)

    def get_login_session_access(self, password: str) -> bool:
        return self.hashed_password == self.hash_password(password)

    def get_pretty_client_info(self) -> str:
        print('CLIENTS PERSONAL INFO:')
        return prettify(vars(self))


if __name__ == "__main__":
    client1 = Client(first_name='John', last_name='Johnson', password='Secret')

    client_password = getpass("Enter the Password: ", stream=sys.stderr)

    if client1.get_login_session_access(password=client_password):
        print('Access granted!')
        client1.get_pretty_client_info()
    else:
        print('Access Denied!')

    client_password = getpass("Enter the Password: ", stream=sys.stderr)
    if client1.get_login_session_access(password=client_password):
        client1.get_pretty_client_info()
    else:
        print('Access Denied!')

