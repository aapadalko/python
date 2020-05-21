a = int(input('Введите число А: '))
b = int(input('Введите число Б: '))
c = int(input('Введите число В: '))
if a > b: print('Свершилоcь!')
elif b > a: print('Да ну!')
else:
    print('А если так: сравним А + В и Б - В')
    x = a + c
    y = b - c
    if x > y: print('Свершилоcь!')
    elif y > x: print('Да ну!')

