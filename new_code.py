import numpy as np
def random_predict(number:int=1) -> int:
    random_number = np.random.randint(1, 101) # загадываем число
    count = 0
    min = 1
    max = 100
    mid=0
    while True:
        count+=1
        mid = round((min+max) / 2) #берём середину диапазона
        
        if mid > random_number:
            max = mid
        elif mid < random_number:
            min = mid
        else:
            
            break #конец игры выход из цикла    
    return(count)

def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)