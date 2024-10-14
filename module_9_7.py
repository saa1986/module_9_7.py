"""Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
и "Составное" в противном случае."""

"""def sum_three(a, b, c):
    return a + b + c

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 1:
            print("Простое")
        else:
            print("Составное")
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

sum_three(2, 3, 5)"""

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Получаем результат выполнения функции
        # Проверяем, является ли результат простым числом
        if result < 2:
            print("Составное")  # Числа меньше 2 не являются простыми
        else:
            for i in range(2, int(result**0.5) + 1):
                if result % i == 0:
                    print("Составное")  # Если число делится на i, оно составное
                    return result
            print("Простое")  # Если не нашли делителей, число простое
        return result  # Возвращаем результат функции
    return wrapper  # Возвращаем обернутую функцию

@is_prime  # Применяем декоратор к функции sum_three
def sum_three(a, b, c):
    return a + b + c  # Складываем три числа

# Примеры использования
result = sum_three(2, 3, 6)  # Выводит: Составное, затем 11
print(result)

#result = sum_three(1, 1, 1)  # Выводит: Составное, затем 3
#print(result)

#result = sum_three(5, 3, 1)  # Выводит: Простое, затем 9
#print(result)

#result = sum_three(3, 5, 7)  # Выводит: Составное, затем 15
#print(result)