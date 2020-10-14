import math


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def largest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError('Wrong factors error.')

    palindromes = []
    for x in range(max_factor, min_factor, -1):
        for y in range(x, min_factor, -1):
            product = x * y
            if is_palindrome(product) and len(palindromes) < 4:
                palindromes.append(product)
    print('products')

    if palindromes:
        max_p = max(palindromes)
        factors = []
        if max_p == 9:
            for i in range(min_factor, max_p+1):
                for j in range(min_factor, max_p+1):
                    if i*j == max_p and sorted([i, j]) not in factors:
                        factors.append([i, j])
        n = math.sqrt(max_p)
        n = math.ceil(n)
        while (max_p % n != 0):
            n += 1
            if max_p % n == 0:
                m = max_p / n
                factors.append([m, n])
        print('factors')
        return max_p, factors
    return None, []


def smallest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError('Wrong factors error.')

    palindromes = []
    for x in range(min_factor, max_factor+1):
        for y in range(min_factor, max_factor+1):
            product = x * y
            if is_palindrome(product) and len(palindromes) < 1:
                palindromes.append(product)

    if palindromes:
        min_p = min(palindromes)
        factors = []
        n = math.sqrt(min_p)
        if min_p % n == 0:
            m = min_p / n
            factors.append([m, n])
        n = math.ceil(n)
        while (min_p % n != 0):
            n += 1
            if (min_p % n == 0):
                m = min_p / n
                factors.append([m, n])
        return min_p, factors
    return None, []


ROWER
rama: skrzynka na baterie / podsiodło / mocowanie dampera / duze boczki / małe boczki/ obudowa sterownika / wahacz - kazdy element ma swoj kolor
przednie koło: model piasty / długość szprych, kolor / model obręczy / rozmiar obręczy / kolor obręczy /  model opony / rozmiar opony
tylnie koło: model piasty / długość szprychy, kolor / model obręczy / rozmiar obręczy / model obręczy / kolor obręczy / rozmiar opony / silnik(nawój, model, chłodzenie, wolnobieg (wartość liczba z końcówką T), [wartość przewinięcia(True, False) jezeli True to data przewinięcia])

amortyzacja: amortyzator przód (model amortyzatora, wielkość koła (26 cali 27.5, 29, 29+), rodzaj osi (20x110, 15x110 i mozliwosc dodania innej)) / tył (model am, długość am, dlugosc sprezyny(151, 241, 240, 270, 300, długość w milimetrach), kolor spręzyny, twartosc sprezyny(300, 400, 550, 600, 650, 700, 850, 1000, 1200, 1300 w jednostceLBS))/ spręzyna dampera - wartosc w LBS(liczbowa, int) / amortyzator model

hamulce:
- przedni (model hamulca, model tarczy, wielkość tarczy)
- tylni (model hamulca, model tarczy, wielkość tarczy)

oświetlenie:
- przód (ilość lampek 1 lub 2, model lampki)
- tył (tak lub nie, a jezeli tak to pozycja albo pozycja i stop - tu bez modelu, bo zawszse jest jeden model lampek)


sterownik:
- model
- prąd z baterii (w amperach, jednostka A)
- prąd fazowy (w amperach)
- PAS (True or False, domyslnie FALSE (klauzula sumienia))

bateria:
- model baterii
- model ogniw
- model BMS (battery management system)
- data wykonania
- wykonana przez
- wartość sekcji (ImageField jpg)

akcesoria:
- model siodełka
- błotniki (True or False domyslnie True)
- wyświetlacz: model wyświetlacza lub BRAK
- manetka (prawa strona / lewa strona (domyślnie PRAWA))
- port USB (True or False domyslnie True)
- GPS (True or False) jezeli True to : wartości ID urządzenia, login, hasło, nr telefonu, odcięcie zasilania (True or False, domyslnie False)
- nózka (True or False)
- ukryty przełącznik mocy (wartosc domyslna jako opis przełącznika)
- kolor gripów
- kolor dodatków
- kolor pedałów
- kolor łańcucha
- rodzaj włącznika: kluczyk / alarm / immobilizer

KLIENT
wzrost
waga
telefon
adres dostawy
adres fakturowy

SERWIS
- data ostatniego serwisu
