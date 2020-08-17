"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
"""

# Схема приема данных от пользователя ( кортеж, т.к. схема практически меняеться редко )
sheme_model=(
    ("Имя", str, "name"),
    ("Фамилия", str, "surname"),
    ("Год рождения", int, "birth_year"),
    ("Город проживания", str, "city"),
    ("email", str, "email"),
    ("Телефон", str, "phone"),
    )

# TODO: Добавить валидаторы на все параметры
def input_data(param_name, param_type):
    """Получаем данные от пользователя
    :param param_name: Текстовое обозначение параметра
    :param param_type: Тип параметра
    :return: Результат принятого параметра
    """
    while True:
        try:
            param = param_type(input(f'Введите "{param_name}": '))
        except:
            print(f'"{param_name}" должно быть как {param_type}')
            continue
        break
    return param

def print_user_data(in_sheme_model, **kwargs):
    """Ввывод данных пользователя на экран
    :param kwargs: именованные аргументы функци
    """
    for sheme_itm in in_sheme_model: print(f'{sheme_itm[0]}: {kwargs[sheme_itm[2]]}')

users_model = []
while True:
    # Добавляем данные пользователя
    continue_answ = input("Хотите добавить пользователя? ( Да ): ")
    if continue_answ.lower() != "да":
        break
    user_model = {sheme_itm[0]:input_data(sheme_itm[0], sheme_itm[1]) for sheme_itm in sheme_model}
    users_model.append(user_model)

    # Вывод  на экран данных пользователя
    print_user_data(sheme_model, 
        name=user_model["Имя"],
        surname=user_model["Фамилия"],
        birth_year=user_model["Год рождения"],
        city=user_model["Город проживания"],
        email=user_model["email"],
        phone=user_model["Телефон"]
        )
