def comparison (line_1, line_2):
    if type(line_1) == type(line_2) == type('str') :
        if len(line_1) > len(line_2) and line_2 != 'learn':
            a =2
            return(a)
        elif line_2 == 'learn':
            a = 3
            return(a)
        a = 1
        return(a)
        
    else:
        a = 0
        return(a)
    

line_1 = input('Введите строку 1:')
line_2 = input('Введите строку 2:')
number = comparison(line_1, line_2)
print ('Ваше число', number)