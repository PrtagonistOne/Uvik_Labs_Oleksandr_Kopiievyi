class ISBNValidationError(Exception):
    def __init__(self, message="ISBN-10 address is not valid!"):
        self.message = message
        super().__init__(self.message)


class ISBNValidator:
    def __call__(self, isbn):
        """Change the position of the entity."""
        print('Validating..')
        if len(isbn) != 10:
            raise ISBNValidationError

        nums = [10 if num == "X" else int(num) for num in isbn]
        checked = sum(nums[num - 1] * num for num in range(1, 11)) % 11
        if checked:
            raise ISBNValidationError
        print('Validated Successfully')

        return isbn


if __name__ == "__main__":
    validate_isbn = ISBNValidator()
    validate_isbn('048665088X')
    validate_isbn('1112223339X')
