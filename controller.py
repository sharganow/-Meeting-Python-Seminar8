import time
import itertools as its
import model as ml
import view as vw

delay = 0.1


def main_menu() -> None:
    action = 'Выберите класс'
    while True:
        try:
            match action:
                case 'Выберите класс':
                    ml.set_school_db(ml.get_classes())
                    choose_class(ml.get_school_db())
                    break
                case _:
                    action = 'Выберите класс'
        except:
            exit(-1)
        time.sleep(delay)


def choose_class(school: list) ->None:
    action = ['Сформируйте класс']
    title = ['Выберите класс в школе с которым будете работать:']
    class_name = vw.get_user_choice(list(its.chain(title, school, action)))
    while True:
        try:
            match class_name:
                case 'Сформируйте класс':
                    break
                case _:
                    ml.set_class_name(class_name)
                    break
        except:
            exit(-1)
        time.sleep(delay)
