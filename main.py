# Пользователь вводит строку из чисел
array = input('Введите числа, разделяя пробелами:\n')

# Разделение строки пробелами и перевод чисел во float
numbers = list(map(float,array.split(' ')))

# Сортировка пузырьком
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


print(numbers)