def evaluate_palindrome_or_symmetrical(value: str) -> dict:
    # sourcery skip: inline-immediately-returned-variable
    value = ''.join(item for item in value if item.isalnum()).lower()
    value_second_part = value[: len(value) // 2].lower()
    value_first_part = value[len(value) // 2:].lower()
    is_both_value_parts_symmetrical = value_second_part == value_first_part

    reversed_value = value[::-1]
    is_palindrome = value == reversed_value

    status_dict = {"Value": f"{value}",
                   "Symmetrical": is_both_value_parts_symmetrical,
                   "Palindrome": is_palindrome}

    return status_dict


if __name__ == "__main__":
    print(evaluate_palindrome_or_symmetrical('khokho'))
    print(evaluate_palindrome_or_symmetrical('amaama'))
    print(evaluate_palindrome_or_symmetrical(input()))
