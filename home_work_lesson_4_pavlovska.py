notes = [] #Задаємо наш список
print('You could enter one of the commands:add, earliest, latest, shortest, longest, exit. ')

#Використаємо цикл з умовою, що програма буде працювати допоки користувач не введе команду 'exit'
while True:
    command = str(input('Please, enter your command: ')).lower () # Зчитуємо команду з консолі та приводимо все до типу стрінг та єдиного регістру
    # Викистовуємо умовні оператори, щоб перевірити яку команду обрав користувач
    if command == 'add':
        notes.append(input('Enter note: ')) # Додаємо елемент в кінець
        print('Your note is added')
    elif command == 'earliest':
        print('From oldest to newest:')
        for notice in notes:
            print(notice)  # За замовчуванням вивід від найстарішої до найновішої, бо ми постійно новий елемент додавали в кінець, тому просто виводимо список
    elif command == 'latest':
        print('From newest to oldest:')
        for notice in notes[::-1]:
            print (notice) # Почнемо з кінця списку
    elif command == 'longest':
        print('From longest to shortest: ')
        for notice in sorted(notes, key=len, reverse=True):
            print (notice) # За замовчуванням по довжині сортує у порядку зростання, тому застосовуємо реверс
    elif command == 'shortest':
        print('From shortest to longest: ')
        for notice in sorted(notes, key=len):
            print (notice) # За замовчуванням по довжині сортує у порядку зростання, тому просто виводимо
    elif command == 'exit':
        break # Якщо 'exit', то завершуємо цикл
    else:
        print('The commands is unknown. Please enter one of the existing commands: add, earliest, latest, shortest, longest, exit')
    # Якщо введена команда, яка не відповідає одній з команд у тілі циклу, виводимо відповідне повідомлення