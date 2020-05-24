a = int(input('Введите число А: '))
b = int(input('Введите число Б: '))
c = int(input('Введите число В: '))
if a > b:
    print('Свершилось!')
elif b > a:
    print('Да ну!')
else:
    print('А если так:')
x = a + b
y = b - c
if x > y:
    print('Свершилось!')
elif y > x:
    print('Да ну!')