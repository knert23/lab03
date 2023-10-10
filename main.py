# Пользователь вводит строку из чисел
array = input('Введите числа, разделяя пробелами:\n')

print('Выберите вариант сортировки:')
print('1. Возрастание')
print('2. Убывание\n')
choose = int(input())

# Разделение строки пробелами и перевод чисел во float
numbers = list(map(float,array.split(' ')))

# Сортировка пузырьком
if choose == 1:
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
elif choose == 2:
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)