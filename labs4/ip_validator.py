from functools import wraps


class IPValidationError(Exception):
    def __init__(self, message="Ip address not valid!"):
        self.message = message
        super().__init__(self.message)


def ip_validator(func):
    @wraps(func)
    def wrapper(ip: str):
        print('Validating..')
        ip_parts = ip.split('.')
        if len(ip_parts) != 4:
            raise IPValidationError
        for ips in ip_parts:
            if len(ips) > 1 and ips[0] == '0':
                raise IPValidationError
            ips = int(ips)
            if 0 >= ips >= 255:
                raise IPValidationError
        return func(ip)

    return wrapper


@ip_validator
def connect_to_ip(ip: str):
    return f"Successfully connected to {ip}!"


print(connect_to_ip('123.45.67.89'), '\n')
print(connect_to_ip('123.045.067.089'))


