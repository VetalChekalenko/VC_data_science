import numpy as np
def random_number(number:int=1) -> int:    #Создаём функцию, которая будет загадывать и отгадывать число
    any_number = np.random.randint(1,101)   #Загаданное число
    count = 0                               #переменная счёчика попыток
    min = 1                                 #переменная начила диапазона
    max = 100                               #переменная окончание диапазона
    middle = 0                              #переменная середины диапазона
    while True:                             #цикл для отгадывания цисла
        count+=1
        middle = round((min+max)/2)         # находим середину диапазона для каждого меняющегося диапазона
        if middle > any_number:             # если середина диапазона меньше загаданного числа
            max = middle                    #новое окончание диапазона равняется середине диапазона
        elif middle < any_number:           #если не выполнено предыдущее условие, то 
            min = middle                    #новое начало диапазона равняется середине диапазона
        else:                               #иначе    
            print (f'Загаданное компьютером число {any_number} отгадано компьютером за {count} попыток')
            break                           #окончание цикла и отгадывания числа
    return (count)

def score_game(random_number) -> int:                       #функция, которая определяет среднее кол-во попыток
    count_lst = []                                          #создаём пустой список, в котором будет хранить каждое значение count
    np.random.seed(1)                                       #инициалруем случайное число
    score = 0
    random_array = np.random.randint(1,101, size=(1000))    #загадываем числа
    for number in random_array:                             #цикл перебора чисел от 1 до 1000
        count_lst.append(random_number(number))             #добавляем каждое значение count в список
    score = int(np.mean(count_lst))                         #находим среднее количество значений в виде целочисленного значения
    print (f'Компьютер находит значение в среднем за {score}')
    return (score)
score_game(random_number)   
