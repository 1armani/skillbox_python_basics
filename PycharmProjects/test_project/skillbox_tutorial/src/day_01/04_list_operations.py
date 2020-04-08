"""
Пример программы для работы со списками

Данные
- есть список из 6 чисел [4, 8, 15, 16, 23, 42]

Сделать
- добавить число 108 в конец списка
- удалить число 15
- вывести длину списка
- вывести сумму всех значений
- вывести последний элемент
- вывести срез элементов с 2 по 4
"""

numbers = [1, 1.3, 2.4, 3, 3.5, 4, 1, 4, 8, 15, 16, 23, 42]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

numbers = [1,2,3,4]


to_index = len(numbers)
from_index = to_index - 10
last10messages = numbers[from_index:to_index + 1]

last10messages = numbers[-10:len(numbers)]


#print(numbers[from_index:to_index + 1])


print(*last10messages, sep= "\n")

#for i in last10messages:
#    print(i)


numbers.reverse()
last10messages = numbers[0:10]
last10messages.reverse()


print(last10messages)
#for last10messages in numbers:


"""print(numbers)

numbers.append(108)
print(numbers)

numbers.remove(15)
print(numbers)

print(sum(numbers))

print(numbers[1])
print(numbers[-1])
print(numbers[2:4])"""
