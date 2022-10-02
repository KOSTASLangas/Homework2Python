# Реализуйте алгоритм перемешивания списка.
import random
arr = []
for x in range(1, 10):
    arr.append(random.randint(1, 100))
print(arr)
i = len(arr) - 1
while i >= 1: 
    j = (random.randint(0, i))
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp
    i -= 1
print(arr)