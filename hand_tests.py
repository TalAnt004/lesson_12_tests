from functions import salary,hello_who

if hello_who('Кирилл') != "Hello, Кирилл":
    print('Ошибка')
else:
    print('Все хорошо')
if hello_who('Олег') != 'Hello, Олег':
    print('Ошибка')
else:
    print("Все правильно")

if salary(5, 500) != 5000:
    print("Ошибка")
else:
    print("Все Правильно")
if salary(2, 300) != 1200:
    print('Ошибка')
else:
    print('Все хорошо')