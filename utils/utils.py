def parse_number_to_password(number):
    number = str(number)
    if len(number) < 4:
        number = "0" * (4 - len(number)) + number
    return number