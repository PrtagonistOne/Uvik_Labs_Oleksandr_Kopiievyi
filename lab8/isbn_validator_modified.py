from dataclasses import dataclass
from functools import wraps


class ISBNValidationError(Exception):
    def __init__(self, message="ISBN-10 address is not valid!"):
        self.message = message
        super().__init__(self.message)


@dataclass
class ISBNValidator:
    isbn: str

    @staticmethod
    def isbn_validator(func):
        @wraps(func)
        def wrapper(isbn: str):
            print('Validating..')
            if len(isbn) != 10:
                raise ISBNValidationError

            nums = [10 if num == "X" else int(num) for num in isbn]
            checked = sum(nums[num - 1] * num for num in range(1, 11)) % 11
            if checked:
                raise ISBNValidationError
            return func(isbn)

        return wrapper

    @staticmethod
    def connect_to_isbn_address(isbn: str):
        return f"Successfully connected to {isbn}!"

    def __call__(self):
        '''Change the position of the entity.'''
        self.isbn_validator(self.connect_to_isbn_address(self.isbn))
        print('Validated Successfully')


if __name__ == "__main__":
    validate = ISBNValidator(isbn='048665088X')
    validate()

    validate.isbn = '1112223339X'

    validate()

    # print(connect_to_isbn_address('048665088X'), '\n')
    #
    # print(connect_to_isbn_address('1112223339X'))
