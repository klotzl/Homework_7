from json import load


def load_students(filename):
    '''Загружает список студентов из файла'''
    with open(filename, mode='r', encoding='utf-8') as file:
        data = load(file)
    return data


def load_professions(filename):
    '''Загружает список  профессий из файла'''
    with open(filename, mode='r', encoding='utf-8') as file:
        data = load(file)
    return data


def get_student_by_pk(pk, data):
    '''Получает словарь с данными студента по его pk'''
    for item in data:
        if pk == item['pk']:
            return item


def get_profession_by_title(title, data):
    '''Получает словарь с инфо о профе по названию'''
    for item in data:
        if title == item['title']:
            return item


def check_fitness(student, profession):
    '''функция, которая получив студента и профессию, возвращает словарь:'''
    set_student = set(student['skills'])
    set_profession = set(profession['skills'])

    has_skills = set_student.intersection(set_profession)
    lacks_skills = set_profession.difference(set_student)

    fit_percent = round(len(has_skills) / len(set_profession) * 100)

    '''{
  "has": ["Python", "Linux"],
  "lacks": ["Docker, SQL"],
  "fit_percent": 50
}'''

    dict_result = {"has": has_skills, "lacks": lacks_skills, "fit_percent": fit_percent}

    return dict_result


def show_result(data, name):
    '''функция прощитывает результаты'''
    str_has = ', '.join(data['has'])
    str_lacks = ', '.join(data['lacks'])

    str_output = f'Пригодность {data["fit_percent"]}% \n' \
                 f'{name} знает {str_has} \n' \
                 f'{name} не знает {str_lacks} \n'

    return str_output
