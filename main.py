# В ОДНОЙ ПАПКЕ С ДАННЫМ ФАЙЛОМ ДОЛЖЕН БЫТЬ СОЗДАН ФАЙЛ data.txt

with open(file="data.txt", mode="r", encoding="utf-8") as data_out:
    content = []
    for line in data_out:
        check = len(line.split())
        if check == 3:
            data, event, part = line.rstrip("\n").split()
            t = (data, event, part)
            content.append(t)
        else:
            data, event = line.rstrip('\n').split()
            t = (data, event)
            content.append(t)

helper = 0
while True:
    if helper == 0:
        print('###Введение###')
        print('#Помощь с работой - 1     #')
        print('#Добавить дату - 2        #')
        print('#Окончить работу кода - 3 #')
        print('#Поиск или вывод дат - 4  #')
        print('Введите цифру ниже: ')
        answer = input()
        if len(answer) < 2 and (answer == '3' or answer == '2' or answer == '1' or answer == '4'):
            helper = int(answer)
            continue
        else:
            print('Введенное вами не является целым числом или не является одним из варианта для выбора.')
            print('###Завершение работы###')
            break
    elif helper == 1:
        print()
        print('###Помощь###')
        print('Для правильного ввода даты нужно ввести в окно для ввода ДАТУ НАЗВАНИЕ. ')
        print('По возможности участника. После чего дата будет находиться в переменной.')
        print('Чтобы интерактировать с введенной вами датой вам необходимо завершить код.')
        print('###Помощь###')
        print('Для того чтобы найти нужную вам дату или нужные даты в диапазоне вам нужно:')
        print('Введите в окно ввода ключевое слово. Ключевым словом считается любое что')
        print('есть в нем. Тоесть ключевым словом может быть год.')
        print()
        helper = 0
    elif helper == 2:
        print()
        print('###Ввод###')
        print('#Введите дату и название по шаблонам:')
        print('XXXX-XX-XX Название_события Название_участника')
        print('Или')
        print('XXXX-XX-XX Название_события')
        print('Другие форматы не допускаются')
        print('#Примеры:')
        print('|1945-05-09|', '|День_Победы|')
        print('|2005-04-11|', '|День_Народного_Единства|', '|Пожарский|')
        print('(Знаки "|" ставить не надо.)')
        answer = input()
        if len(answer.split()) == 3:
            answer_number, answer_name, answer_member = answer.split()
            t = (answer_number, answer_name, answer_member)
            content.append(t)
        else:
            answer_number, answer_name = answer.split()
            t = (answer_number, answer_name)
            content.append(t)
        print()
        helper = 0
    elif helper == 3:
        print('###Завершение работы###')
        print('Спасибо за использование программы.')
        break
    elif helper == 4:
        print()
        print('###Вывод/Поиск###')
        print('#Вывести все даты - 1#')
        print('#Поиск даты - 2      #')
        print('#Выйти из поиска - 3 #')
        print('#Введите ваш ответ ниже:')
        print()
        answer = input()
        if len(answer) < 2 and (answer == '1' or answer == '2' or answer == '3'):
            if answer == '1':
                print()
                print('###Вывод_Дат###')
                for row in content:
                    print(*row)
                print('###Вывод_Дат###')
                print()
            if answer == '2':
                print('###Поиск###')
                print('#Введите ключевую слово для поиска ниже:')
                answer = input()
                print()
                print('###Ответ###')
                for index_1 in range(len(content)):
                    entire = content[index_1]
                    if len(entire) == 3:
                        for index_2 in range(3):
                            elem = content[index_1][index_2]
                            str(elem)
                            if answer in elem:
                                print(*content[index_1])
                    else:
                        for index_2 in range(2):
                            elem = content[index_1][index_2]
                            str(elem)
                            if answer in elem:
                                print(*content[index_1])
                print('###Ответ###')
                print()
            if answer == '3':
                helper = 0
        else:
            print('###Завершение работы###')
            print('Введенное вами не является целым числом или не является одним из варианта для выбора.')
            break
new_content = []
for row in content:
    s = ''
    for elem in row:
        s += elem + ' '
    s = s[:-1] + '\n'
    new_content.append(s)

with open(file='data.txt', mode='w', encoding='UTF-8') as data_out:
    data_out.writelines(new_content)
