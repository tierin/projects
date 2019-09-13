user_age = int(input())


def define_by_age_what_people_do():
    if user_age < 7:
        return 'Пользователь должен учиться в дестком саду'
    elif 7 <= user_age < 18:
        return 'Пользователь должен учиться в школе'
    # ageism detected
    elif 18 < user_age <= 23:
        return 'Пользователь должен учиться в ВУЗе'
    elif 23 < user_age <= 65:
        return 'Пользователь должен работать'


doing_by_age = define_by_age_what_people_do()
print(doing_by_age)