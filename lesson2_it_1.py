def many_years (age):
    if age <= 7 :
        a = 'учитесь в детском саду'
        return(a)
    elif age <= 17 :
        a = 'учитесь в школе'
        return(a) 
    elif age <= 25 :
        a = 'учитесь в ВУЗе'
        return(a)
    else:
        a = 'работайте'
        return(a)

age = int(input('Введите Ваш возраст:'))
b = many_years(age)
c = f'Ваш возраст {age},{b}'
print(c)