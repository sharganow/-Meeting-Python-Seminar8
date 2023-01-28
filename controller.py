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
                    action = 'Выберите предмет'
                case 'Выберите предмет':
                    choose_subject(ml.get_class_db())
                    action = 'Вызовите ученика'
                case 'Вызовите ученика':
                    call_pupil(ml.get_class_db(), ml.get_subject_name())
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
                    ml.set_class_db(ml.open_class_db(ml.get_class_name()))
                    break
        except:
            exit(-1)
        time.sleep(delay)


def choose_subject(class_db: dict) -> None:
    action = ['Сформируйте класс']
    subject_list = ml.get_subjects_list(class_db)
    title = ['Выберите предмет для проведения занятия:']
    subject_name = vw.get_user_choice(list(its.chain(title, subject_list, action)))
    while True:
        try:
            match subject_name:
                case 'Сформируйте класс':
                    break
                case _:
                    ml.set_subject_name(subject_name)
                    break
        except:
            exit(-1)
        time.sleep(delay)


def call_pupil(class_db: dict, subject: str) -> None:
    action = ['Сформируйте класс']
    pupil_list = ml.get_pupil_list(class_db, subject)
    title = ['Выберите ученика для контрольной проверки знания пройденого материала:']
    active_pupil = vw.get_user_choice(list(its.chain(title, pupil_list, action)))
    while True:
        try:
            match active_pupil:
                case 'Сформируйте класс':
                    break
                case _:
                    ml.set_active_pupil(active_pupil)
                    break
        except:
            exit(-1)
        time.sleep(delay)