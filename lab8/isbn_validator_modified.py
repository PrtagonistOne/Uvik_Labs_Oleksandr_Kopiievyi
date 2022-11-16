class ISBNValidationError(Exception):
    def __init__(self, message="ISBN-10 address is not valid!"):
        self.message = message
        super().__init__(self.message)


class ISBNValidator:
    def __init__(self, *parameters):
        self.parameters = parameters

    def __call__(self, func):
        def wrapper(isbn: str):
            print('Validating..', *self.parameters)
            if len(isbn) != 10:
                raise ISBNValidationError
            nums = [10 if num == "X" else int(num) for num in isbn]
            checked = sum(nums[num - 1] * num for num in range(1, 11)) % 11
            if checked:
                raise ISBNValidationError
            return func(isbn)
        return wrapper


@ISBNValidator("Very validating...", 'Very very Validating...')
def connect_to_isbn_address(isbn: str):
    return f"Successfully connected to {isbn}!"


if __name__ == "__main__":
    print(connect_to_isbn_address('048665088X'))
    print(connect_to_isbn_address('1112223339X'))

