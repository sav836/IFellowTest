import random
array_size = 10
random_numbers = [random.random() for i in range(array_size)]

max_value = max(random_numbers)
min_value = min(random_numbers)
average_value = sum(random_numbers) / len(random_numbers)

print("Массив:", [round(num, 4) for num in random_numbers])
print("Максимум:", round(max_value, 4))
print("Минимум:", round(min_value, 4))
print("Среднее:", round(average_value, 4))