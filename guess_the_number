
# Программа по угадыванию числа с подсказками
import random
print("\tЗдравствуй дружок!\nСейчас я загадаю число от 1 до 100, а ты его должен будешь отгадать")
counter = 1
number = random.randint(1,100)
x = 0
while number != x:
    x = int(input("Какое число загадано? "))
    if x > number:
        print("Загаданное число меньше")
    elif x < number:
        print("Загаданное число больше")
    counter +=1
print("Ура! Ты отгадал! Это число ", number, "\nТы отгадал его за ", counter, "попыток")

input("\n\nНажмите Enter для выхода")
