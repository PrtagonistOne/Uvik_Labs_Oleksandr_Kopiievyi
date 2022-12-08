from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)


class IPValidationError(Exception):
    def __init__(self, message="Ip address not valid!"):
        self.message = message
        super().__init__(self.message)


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class IPValidator(Validator):
    def __init__(self, ip: str):
        self.ip = ip

    def validate(self, value):
        print('Validating..')
        ip_parts = value.split('.')
        if len(ip_parts) != 4:
            raise IPValidationError
        for ips in ip_parts:
            if len(ips) > 1 and ips[0] == '0':
                raise IPValidationError
            ips = int(ips)
            if 0 >= ips >= 255:
                raise IPValidationError
        print(f"Successfully connected to {value}!")


class GetInternetAccess:
    ip_address = IPValidator(ip='127.0.0.0')

    def __init__(self, ip_address):
        self.ip_address = ip_address

    def __repr__(self):
        return self.ip_address


if __name__ == "__main__":
    GetInternetAccess('123.45.67.89')

    GetInternetAccess('123.045.067.089')
