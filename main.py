from random import choice

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = sorted(students)

list_ = {}
for student, grade in zip(my_list, grades):
    sred = sum(grade) / len(grade)
    list_[student] = sred



is_running = True
def all_list():
    print(list_)
    return 0

def bad_students():
    for key, value in list_.items():
        if value < 4:
            print(key, ": " , value)
    return 0

def good_students():
    for key, value in list_.items():
        if value >= 4:
            print(key, ": " , value)
    return 0


while is_running == True:
    print('Добро пожаловать в подсчёт среднего балла!')
    print('1.Вывести весь список!')
    print('2.Показать студентов с утешительным баллом!')
    print('3.Показать студентов с хорошим баллом!')
    print('4.Выйти из программы!')

    choice = input('Выберите действие!')
    if choice == '1':
        all_list()
    elif choice == '2':
        bad_students()
    elif choice == '3':
        good_students()
    elif choice == '4':
        is_running = False
    else:
        print('Вы пытаетесь зайти куда-то не туда)')
        is_running = False
