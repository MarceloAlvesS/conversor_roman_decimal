roman_to_decimal = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

roman_number = input('Digite um número romano: ')
decimal_number = 0
for i, roman in enumerate(roman_number):
    if roman_to_decimal.get(roman):
        if i != len(roman_number)-1 and roman_to_decimal[roman] < roman_to_decimal[i+1]:
            continue
        decimal_number += roman_to_decimal[roman]
    else:
        break


print(decimal_number)
