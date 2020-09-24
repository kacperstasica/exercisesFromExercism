def classify(number):
    if number <= 0:
        raise ValueError('Number rejected - not a natural number')
    # divisors = []
    divisors = (number // i for i in range(1, number) if number % i == 0)
    # for divisor in range(1, number):
    #     if number % divisor == 0:
    #         divisors.append(divisor)
    summary = sum(divisors)
    if summary == number:
        return 'perfect'
    elif summary > number:
        return 'abundant'
    return 'deficient'


def factors(n):
    return [x for x in range(1, n+1) if n % x == 0]