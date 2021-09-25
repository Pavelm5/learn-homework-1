"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Как дела?": "Хорошо!",
 "Что делаешь?": "Программирую", 
 "Как успехи?": "Прибавляются с каждым днём", 
 "Как настроение?": "Рабочее"
}

def ask_user(questions_and_answers):
    """
    Замените pass на ваш код
    """
    while True:
        user_sai = input('Есть вопрос? Задавай  ')
        print(get_answer(questions_and_answers, user_sai)) 


def get_answer(questions_and_answers, quests):
    return questions_and_answers.get(quests,"Спроси другое")

  
      

   

if __name__ == "__main__":
    ask_user(questions_and_answers) 

  