# Цикл while задание

def ask_user (question, questions):
    
    while True:
        user_say = input(question)
        if user_say == "Нет":    
            break
        else:
            term = input("Задай вопрос программе:")
            if term in questions:
                print (questions[term]) 
            else:
                print(f'Я не знаю что ответить на вопрос {term}')
            # print(f'Сам ты {user_say}')
    b = "Все пока"
    return b

questions = {'Как дела?': 'Хорошо!', "Что делаешь?": "Программирую"}
a = ask_user ("Будут еще вопросы?", questions)
print(a)