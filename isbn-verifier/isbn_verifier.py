def is_valid(isbn):
    if len(isbn) != 13:
        if len(isbn) != 10:
            return False

    isbn_list = []
    for i in isbn:
        if i.isdigit():
            isbn_list.append(int(i))
        elif i == 'X':
            if 'X' == isbn[-1]:
                isbn_list.append(10)

    multiplier = 10
    check_list = []
    for number in isbn_list:
        check_list.append(number * multiplier)
        multiplier -= 1

    if sum(check_list) % 11 == 0:
        return True
    return False
