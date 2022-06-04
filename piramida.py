ctorona_a = float(input('Введите 1 сторону = '))
ctorona_b = float(input('Введите 2 сторону = '))
ctorona_c = float(input('Введите 3 сторону = '))
if ctorona_a+ctorona_b>ctorona_c and ctorona_b+ctorona_c>ctorona_a and ctorona_a+ctorona_c>ctorona_b:
    print('Такой треугольник существует')
    if ctorona_a==ctorona_b and ctorona_b==ctorona_c:
        print('Треугольник равностороний')
    elif ctorona_a==ctorona_b or ctorona_b==ctorona_c or ctorona_a==ctorona_c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
