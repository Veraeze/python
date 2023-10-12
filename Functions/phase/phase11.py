def check_number(integer: int, integers: list) -> bool:
    for number in integers:
        if number == integer:
            return True
    return False
