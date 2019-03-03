# Цикл for задание
school = [{'school_class':'4а', 'scores':[3,4,4,5,2]},
        {'school_class':'4б', 'scores':[4,5,3,4,4]},
        {'school_class':'4в', 'scores':[5,3,3,5,4]},
        {'school_class':'4г', 'scores':[3,4,5,4,5]}]

# Найдем средний балл по всей школе
list_a = 0 # сумма оценок всей школы
list_b = 0 # количество оценок всей школы

'''for i in school:  
  list_b += len(i['scores'])
  for d in i['scores']:
    list_a += d
c = list_a / list_b # средний балл всей школы
print (f'Средний балл по всей школе = {c}')'''

# Найдем средний балл по каждому классу
amount = 0 # Сумма оценок
amount_school = 0 # Сумма оценок всей школы
c = 0
for dictionary in school :
    a = dictionary['school_class'] # классы
    b = dictionary['scores']  # список оценок 
    average_mark = sum(b) / len(b)  # Средний бал по каждому класс
    amount_school += sum(b)
    c += len(b)
    print (f'Средняя оценка класса {a} = {average_mark}')
average_mark_school = amount_school / c
print (f'Средний балл по всей школе = {average_mark_school}')