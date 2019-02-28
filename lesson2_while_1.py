# Цикл while задание

def ask_user (question):
    
    while True:
        user_say = input(question)
        if user_say == "Хорошо":    
            break
        else:
            print(f'Сам ты {user_say}')
    b = "Все пока"
    return b
a = ask_user ("Как дела?")
print(a)