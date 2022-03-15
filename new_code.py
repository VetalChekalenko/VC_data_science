err = {
        1: 'пароль слишком короткий',
        2: 'пароль слишком длинный',
        3: 'в пароле отсутсвуют цифры',
        4: 'в пароле отсутсвуют строчные буквы',
        5: 'в пароле отсутсвуют прописные буквы',
    }
def check_pass(pswd):
    a=len(pswd)
    if a < 8:
        print (f'{err[1]}')
    elif a > 8:
        print (f'{err[2]}')
    else:
        print  (f'{err[3]}')   
    return print (a)
print (check_pass('1234567'))
print (check_pass('12345678'))
print (check_pass('123456789'))