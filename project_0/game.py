from tokenize import Number
import numpy as np
number = np.random.randint(1,101)
count = 0
while True:
    count += 1
    predict_number = int(input("Угадайте число от 1 до 100: "))
    if number > predict_number:
        print ("Число больше: ")
    elif number < predict_number:
        print ("Число меньше")
    else:
        print ("Число угадано")
        break 