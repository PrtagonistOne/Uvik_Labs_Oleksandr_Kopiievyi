from functools import wraps


class ISBNalidationError(Exception):
    def __init__(self, message="ISBN-10 address is not valid!"):
        self.message = message
        super().__init__(self.message)


def isbn_validator(func):
    @wraps(func)
    def wrapper(isbn: str):
        print('Validating..')
        if len(isbn) != 10:
            raise ISBNalidationError

        nums = [10 if num == "X" else int(num) for num in isbn]
        checked = sum(nums[num - 1] * num for num in range(1, 11)) % 11
        if checked:
            raise ISBNalidationError
        return func(isbn)

    return wrapper


@isbn_validator
def connect_to_isbn_address(isbn: str):
    return f"Successfully connected to {isbn}!"


print(connect_to_isbn_address('048665088X'), '\n')

print(connect_to_isbn_address('1112223339X'))
