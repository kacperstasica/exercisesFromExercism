def is_armstrong_number(number):
    number_to_str = str(number)
    power = len(number_to_str)
    arr = []
    for num in number_to_str:
        num_to_pow = int(num)**power
        arr.append(num_to_pow)
    if sum(arr) == number:
        return True
    return False
