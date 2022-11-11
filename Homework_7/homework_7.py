from functions import *

if __name__ == '__main__':
    file_students = 'students.json'
    file_professions = 'professions.json'

    data_students = load_students(file_students)
    data_professions = load_professions(file_professions)

    user_pk = int(input('Введите номер студента \n'))
    '''получить ввод pk пользователя'''
    student = get_student_by_pk(user_pk, data_students)

    if student:
        '''Если такой студент есть – выведите информацию о пользователе'''
        print(f'Студент {student["full_name"]}')
        str_skills = ', '.join(student["skills"])
        print(f'Знает {str_skills}')
    else:
        '''Если такого студента нет - завершитесь'''
        print('У нас нет такого студента')
        quit()

    title = input('Выберите специальность для оценки студента \n')
    '''Получите ввод title профессии '''
    profession = get_profession_by_title(title, data_professions)
    '''Проверьте существование такой профессии
Если да – получите соответствие с помощью  check_fitness'''

    if not profession:
        '''Если нет – завершитесь'''
        print('У нас нет такой специальности')
        quit()

    data = check_fitness(student, profession)
    print(show_result(data, student['full_name']))
