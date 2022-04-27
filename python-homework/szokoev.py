def is_leap(user_input_year):
    leap = False

    if year % 400 == 0 and year % 4 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 100 == 0:
        leap = False

    if leap:
        print('Szökőév!')
    else:
        print('Nem szökőév!')

    return leap


for i in range(4):
    year = int(input())
    is_leap(year)
    continue
