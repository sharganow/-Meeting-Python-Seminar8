import time
import os

active_pupil = str
subject_name = str
class_name = str
class_db = dict()
school_db = list()
endClassFile = ".class"


def get_active_pupil() -> str:
    global active_pupil
    return active_pupil


def set_active_pupil(pupil: str) -> None:
    global active_pupil
    active_pupil = pupil


def get_subject_name() -> str:
    global subject_name
    return subject_name


def set_subject_name(name: str) -> None:
    global subject_name
    subject_name = name


def get_class_db() -> dict:
    global class_db
    return class_db


def set_class_db(clss: dict) -> dict:
    global class_db
    class_db = dict.copy(clss)


def get_class_name() -> str:
    global class_name
    return class_name


def set_class_name(name: str) -> None:
    global class_name
    class_name = name


def get_school_db() -> list:
    global school_db
    return school_db


def set_school_db(school: list) -> None:
    global school_db
    school_db = school[:]


def get_classes() -> list:
    school = list()
    school = os.listdir()
    # print(school)
    school_copy = school[:]
    for i in range(len(school_copy) - 1, -1, -1):
        if school_copy[i].lower().endswith(endClassFile):
            school_copy[i] = school_copy[i].lower()[:-len(endClassFile)]
            leter = school_copy[i][-1]
            if 'Ё' <= leter <= 'ё':
                try:
                    class_level = int(school_copy[i][:-1])
                except:
                    class_level = -1
                if 0 <= class_level <= 11:
                    school[i] = school[i].upper()[:-len(endClassFile)]
                    continue
        not_a_class = school.pop(i)
        # print(not_a_class)
    return school


def open_class_db(class_name_: str) -> dict:
    class_dbl = dict()
    class_f = str
    try:
        with open(class_name_ + endClassFile, 'r', encoding='UTF-8') as file:
            class_f = file.read()
    except:
        return []
    class_f = [i for i in class_f.split('\n')]
    for i, pupil in enumerate(class_f):
        if pupil[0] == '{' and pupil[-1] == '}':
            index_end_name = pupil.index(':')
            name = pupil[1:index_end_name]
            class_dbl[name] = get_pupil_journal(pupil[index_end_name + 1:-1])
    return class_dbl


def get_pupil_journal(jrnl: str) -> dict:
    jrnl_dict = dict()
    if jrnl[0] == '{' and jrnl[-1] == '}':
        jrnl_lst = [sub for sub in jrnl[1:-1].split(',')]
        for i, sbjct in enumerate(jrnl_lst):
            index_end_name = sbjct.index(':')
            subject = sbjct[:index_end_name]
            if sbjct[index_end_name + 1] == '[' and sbjct[-1] == ']':
                grades = [i for i in sbjct[index_end_name + 2:-1].split(',')]
                jrnl_dict[subject] = grades
    return jrnl_dict


def get_subjects_list(class_dbp: dict) -> list:
    subjects = list()
    pupils = [pupil for pupil in class_dbp.keys()]
    for i, pupil in enumerate(pupils):
        for subject in class_dbp[pupil].keys():
            if subject not in subjects:
                subjects.append(subject)
    for i, pupil in enumerate(pupils):
        pupil_subjects = [subj for subj in class_dbp[pupil].keys()]
        for j, subject in enumerate(subjects):
            if subject not in pupil_subjects:
                class_dbp[pupil][subject] = ['']
    set_class_db(class_dbp)
    return subjects


def get_pupil_list(class_dbp: dict, subject: str) -> list:
    pupil_list = list()
    tab = '\t'
    len_tab = 4
    pupils = [pupil for pupil in class_dbp.keys()]
    max_len = len(pupils[0])
    for i, pupil in enumerate(pupils):
        max_len = len(pupil) if len(pupil) > max_len else max_len
    if max_len % len_tab < 3:
        max_len += len_tab
    for i, pupil in enumerate(pupils):
        need_to_add = (max_len - len(pupil)) // len_tab
        pupil_str = pupil + tab * need_to_add + '   [ '
        for j, grade in enumerate(class_dbp[pupil][subject]):
            pupil_str += grade + ' '
        pupil_str += ']'
        pupil_list.append(pupil_str)
    return pupil_list


def unite_lists(one: list, two: list) -> list:
    for i, d in enumerate(two):
        one.append(d)
    return one
