# Цикл for задание
school = [{'school_class':'4а', 'scores':[3,4,4,5,2]},
        {'school_class':'4б', 'scores':[4,5,3,4,4]},
        {'school_class':'4в', 'scores':[5,3,3,5,4]},
        {'school_class':'4г', 'scores':[3,4,5,4,5]}]

# Найдем средний балл по всей школе
list_a = 0 # сумма оценок всей школы
list_b = 0 # количество оценок всей школы

for i in school:    
  for d in i['scores']:
    list_a += d
    list_b += 1
c = list_a / list_b # средний балл всей школы
print (f'Средний балл по всей школе = {c}')

# Найдем средний балл по каждому классу
amount = 0 # Сумма оценок
for dictionary in school :
    a = dictionary['school_class'] # классы
    b = dictionary['scores']  # список оценок 
    # переберем элементы в списке оценок и найдем их сумму
    for i in b :
        amount += i
    average_mark = amount / len(b)  # Средний бал по каждому класс
    amount = 0
    print (f'Средняя оценка класса {a} = {average_mark}')
