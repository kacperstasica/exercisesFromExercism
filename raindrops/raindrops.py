def convert(number):
    result = ''
    if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        if number % 3 == 0:
            result += 'Pling'
        if number % 5 == 0:
            result += 'Plang'
        if number % 7 == 0:
            result += 'Plong'
    else:
        return str(number)
    return result
