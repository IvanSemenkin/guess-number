from random import randint
import time
points = 0
attempts = 1
print("Привет!")
game_n = input("Поехали?")
if game_n != "нет":
    period = int(input("Выбери сколько у тебя время на игру (в секундах)"))
    print("И так давай сыграем в игру!")
    print("Игра называется Угадайка!!!")
    print("Будут подсказки > больше, < меньше")
    print("Правила игры: угадай загаданное число компьютером!!! ")
    print("Тебе будут начисляться 2 балла за правильный ответ")
    print("Введи -1 если сдаешься")
    print("Будут сниматься 1 бал если ты сдался или закончились", period, "секунд")
    print("У тебя на это ", period,"секунд")
    print("Числа будут от 0 до скольки ты выберешь")
    game = input("Хочешь съиграть в такую игру?")
    from_1 = 0
    to = int(input("Числа будут от 0 до скольки ты сейчас выберешь"))
while game != "нет":
    now = time.clock()
    time_spent = 0
    number = randint(from_1, to)
    answer = int(input("Введите ваш вариант ответа:"))
    while answer != number and time_spent < period and answer != -1:
        if answer > number:
            print("Ваше число больше загаданного")
        else:
            print("Ваше число меньше загаданного")
        answer = int(input("Введите ваш вариант ответа:"))
        time_spent = time.clock() - now
        attempts = attempts + 1
    if answer == -1:
        print("Правильный ответ был: ", number)
        points = points - 1
        print("Тебе штраф -1 очко. Ты сдался. Общее количество балов: ", points)
    else:    
        if time_spent < period:
            print("Ты угадал молодец!!! Это", number)
            points = points + 2
        else:
            print("Врямя закончилось.Ты не угадал. :( Это было ", number)
            points = points - 1
            print("Тебе штраф -1 очко. Время кончилось. Общее количество балов: ", points)
    print("Количество попыток", attempts)
    print("Потрачено времени: ", time_spent)
    print("Ты набрал очков: ", points)  
    game = input("Хочешь ещё сыграть в игру Угадайка")
print("Ты набрал очков: ", points)
print("Пока! Было весело!!!")