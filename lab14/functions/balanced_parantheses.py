def check_balanced_parentheses(my_string):
    brackets = ['()', '{}', '[]']
    while any(x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')
    print(get_executing_module_name())
    return not my_string


def get_executing_module_name() -> str:
    return __name__


if __name__ == "__main__":
    print(check_balanced_parentheses('{[]{()}}'))
    print(check_balanced_parentheses('[{}{}(]'))
    print(check_balanced_parentheses('{][{()}}'))
