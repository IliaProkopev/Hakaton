accounts = open('accounts.txt', 'r')
listok = accounts.readlines()
alogin = []
for i in listok:
    alogin.append(i.split(' ')[0])
accounts.close()

print('Добро пожаловать в онлайн-магазин "Пятёрочка"!')
print('Для начала работы Вам необходимо авторизоваться или зарегистрироваться.')
print('Введите слово "Вход", чтобы авторизоваться, или "Регистрация", чтобы создать аккаунт')

begin = input()

if begin == 'Вход':
    accounts = open('accounts.txt', 'r')
    acc = accounts.readlines()
    while 1:    
        print('Введите логин:')
        login = input()
        for i in acc:
            stroka = i
            if stroka.split(' ')[0] == login:
                break
        if stroka.split(' ')[0] != login:
            print('Пользователя с таким логином не существует!')
        else:
            break
    pswrdin = stroka.split(' ')[1]
    pswrd = ''
    while pswrd != pswrdin:
        print('Введите пароль:')
        pswrd = input()
        if pswrd == pswrdin:
            print('Добро пожаловать, ' + stroka.split(' ')[2][0:(len(stroka.split(' ')[2]) - 1)] + '!')
            break
        elif pswrd != pswrdin:
            print('Неверный пароль!')
elif begin == 'Регистрация':
    accounts = open('accounts.txt', 'a+')
    password = 0
    password2 = 1
    while 1:
        print('Придумайте логин:')
        login = input()
        for i in alogin:
            l = i
            if login == i:
                print('Логин уже занят!')
                break
        if l != login:
            break
    one = [login]
    while password != password2:
        print('Придумайте пароль:')
        password = input()
        print('Введите пароль ещё раз:')
        password2 = input()
        if password == password2:
            one.append(password)
        else:
            print('Пароли не совпадают!')
    print('Введите Ваше имя:')
    one.append(input())
    accounts.write(one[0] + ' ')
    accounts.write(one[1] + ' ')
    accounts.write(one[2])
    accounts.write('\n')
    stroka = one[0] + ' ' + one[1] + ' ' + one[2] + '\n'
    print('Добро пожаловать, ' + one[2] + '!')
else:
    print('Error')

accounts.close()

while 1:
    print('Чтобы выбрать какой-либо пункт, введите соответсвующую цифру.')
    print('1. Каталог товаров\n2. Параметры учётной записи\n3. Корзина\n4. Выход')
    begin = input()
    if begin == '4':
        break                       #выход из программы
    elif begin == '1':
        catalog = open('catalog.txt', 'r')
        cat = catalog.readlines()
        last = cat[-1]
        cat.pop()
        for i in cat:
            print(i[0:(len(i) - 1)])
        print(last)
        print('0. Назад')
        b = input()
        if b == '1':
            x = open("rychki.txt", "r")
            cat = x.readlines()
            last = cat[-1]
            cat.pop()
            pp = '0'
            while 1:
                for i in cat:
                    if int(i.split(' ')[2]) >= int(pp):
                        print(i[0:(len(i) - 1)])
                if int(last.split(' ')[2]) >= int(pp):
                    print(last)
                print('S. Фильтр по цене')
                obj = input()
                if obj == 'S':
                    print('1. Цена от ...\n')
                    p = input()
                    if p == '1':
                        print('Введите цену:')
                        pp = input()
                if obj != 'S':
                    break
            if obj == '1':
                price = cat[int(obj) - 1].split(' ')[2]
            print('Введите количество:')
            num = input()
            pricekorzina = int(num)*int(price)   #переменая считает стоимость выбранных товаров в корзине
            korzina = open('korzina.txt', 'w+')
            korzina.write(cat[int(obj) - 1].split(' ')[1])   #записываем название товара в корзину
            korzina.close()
        if b == "2":
            y = open("tetradi.txt","r")
            cat = y.readlines()
            last = cat[-1]
            cat.pop()
            pp = '0'
            while 1:
                for i in cat:
                    if int(i.split(' ')[2]) >= int(pp):
                        print(i[0:(len(i) - 1)])
                if int(last.split(' ')[2]) >= int(pp):
                    print(last)
                print('S. Фильтр по цене')
                obj = input()
                if obj == 'S':
                    print('1. Цена от ...\n')
                    p = input()
                    if p == '1':
                        print('Введите цену:')
                        pp = input()
                if obj != 'S':
                    break
            if obj == '2':
                price = cat[int(obj) - 1].split(' ')[2]
            print('Введите количество:')
            num = input()
            pricekorzina = int(num)*int(price)   #переменая считает стоимость выбранных товаров в корзине
            korzina = open('korzina.txt', 'w+')
            korzina.write(cat[int(obj) - 1].split(' ')[1])   #записываем название товара в корзину
            korzina.close()
        if b == "3":
            z = open("dnevniki.txt","r")
            cat = z.readlines()
            last = cat[-1]
            cat.pop()
            pp = '0'
            while 1:
                for i in cat:
                    if int(i.split(' ')[2]) >= int(pp):
                        print(i[0:(len(i) - 1)])
                if int(last.split(' ')[2]) >= int(pp):
                    print(last)
                print('S. Фильтр по цене')
                obj = input()
                if obj == 'S':
                    print('1. Цена от ...\n')
                    p = input()
                    if p == '1':
                        print('Введите цену:')
                        pp = input()
                if obj != 'S':
                    break
            if obj == '1':
                price = cat[int(obj) - 1].split(' ')[2]
            print('Введите колличество:')
            num = input()
            pricekorzina = int(num)*int(price)   #переменая считает стоимость выбранных товаров в корзине
            korzina = open('korzina.txt', 'w+')
            korzina.write(cat[int(obj) - 1].split(' ')[1])   #записываем название товара в корзину
            korzina.close()
        elif b == '0':
            #нужно придумать какую-то переменную для дальнейшего определения действий кода!
            break
    elif begin == '2':
        print('1. Изменить имя (' + stroka.split(' ')[2][0:(len(stroka.split(' ')[2]) - 1)] + ')')
        print('2. Изменить логин (' + stroka.split(' ')[0] + ')')
        print('3. Изменить пароль (' + stroka.split(' ')[1] + ')')
        print('4. Назад')
        b = input()
        if b == '4':
            1
        elif b == '1':
            accounts = open('accounts.txt', 'r')
            al = accounts.readlines()
            accounts.close()
            print('Введите новое имя:')
            name = input()
            strokanew = stroka.replace(stroka.split(' ')[2], name + '\n')
            al = list(map(lambda x: x if x != stroka else strokanew, al))
            accounts = open('accounts.txt', 'w')
            for i in range(len(al)):
                accounts.write(al[i])
            accounts.close()
            print('Имя успешно изменено!')
        elif b == '2':
            accounts = open('accounts.txt', 'r')
            al = accounts.readlines()
            accounts.close()
            print('Придумайте новый логин:')
            name = input()
            strokanew = stroka.replace(stroka.split(' ')[0], name)
            al = list(map(lambda x: x if x != stroka else strokanew, al))
            accounts = open('accounts.txt', 'w')
            for i in range(len(al)):
                accounts.write(al[i])
            accounts.close()
            print('Логин успешно изменён!')
        elif b == '3':
            accounts = open('accounts.txt', 'r')
            al = accounts.readlines()
            accounts.close()
            print('Придумайте новый пароль:')
            name = input()
            strokanew = stroka.replace(stroka.split(' ')[1], name)
            al = list(map(lambda x: x if x != stroka else strokanew, al))
            accounts = open('accounts.txt', 'w')
            for i in range(len(al)):
                accounts.write(al[i])
            accounts.close()
            print('Пароль успешно изменён!')
    elif begin == '3':
        print('Товары в вашей корзине:')
        korzina = open('korzina.txt', 'r')
        print(korzina.readlines())
        korzina.close
        print('Общая стоимость: ', pricekorzina)