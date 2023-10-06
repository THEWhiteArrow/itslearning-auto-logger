def parse_number_to_password(number) -> str:
    """
    Parse a number to a password.
    @param number: The number to parse.
    @return: The parsed number.
    """
    number = str(number)
    if len(number) < 4:
        number = "0" * (4 - len(number)) + number
    return number