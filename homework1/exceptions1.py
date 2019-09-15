
questions_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Ты кто?": "Конь в пальто",
                     "Зачем ты здесь?": "Я не знаю", "Почему нельзя делить на ноль?": "Может порваться ткань бытия",
                     "Какого цвета трава?": "Я никогда ее не видел. Может быть, голубая?!",
                     "Кто умеет задавать вопросы?": "Точно не Катя..."}


def ask_user():

    try:
        while True:
            user_input = input('Как дела?\n')
            if user_input == 'Хорошо':
                break
            if user_input in questions_answers.keys():
                print(questions_answers.get(user_input))
    except KeyboardInterrupt:
        print('Пока!')


ask_user()

