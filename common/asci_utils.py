def is_ascii_letter(number):
    return is_capital_letter(number) or is_small_letter(number)


def is_capital_letter(number):
    return 90 >= number >= 65


def is_small_letter(number):
    return 122 >= number >= 97


def is_enter(number):
    return number == 10 or number == 13


def is_space(number):
    return number == 32
