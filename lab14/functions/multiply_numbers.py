def get_multiplied_numbers(x, y):
    num1, num2 = x, y

    def scuffed_multiplication(x, y):
        total_val = 0
        for _ in range(y):
            total_val += x
        return total_val

    if isinstance(num1, float) or isinstance(num2, float):
        if isinstance(num1, float) and isinstance(num2, float):
            decimal_point_length = len(str(num1).split('.')[-1]) + len(str(num2).split('.')[-1])
        elif isinstance(num1, float) and isinstance(num2, int):
            decimal_point_length = len(str(num1).split('.')[-1])
        else:
            decimal_point_length = len(str(num2).split('.')[-1])

        int_x = int(str(num1).replace('.', ''))
        int_y = int(str(num2).replace('.', ''))
        numbers_multiplied = str(scuffed_multiplication(int_x, int_y))
        float_number_formatted = ''.join(f'{val}.' if num_count == decimal_point_length
                                      else val for num_count, val in enumerate(numbers_multiplied[::-1], start=1))
        return float(float_number_formatted[::-1])
    else:
        return scuffed_multiplication(num1, num2)


if __name__ == "__main__":
    print(get_multiplied_numbers(5.5, 5.55))
    print(get_multiplied_numbers(2.62, 1.1))
