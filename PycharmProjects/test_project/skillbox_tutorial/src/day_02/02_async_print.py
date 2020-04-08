"""
Пример программы для работы с асинхронностью

Данные
- пользователь вводит число X

Сделать
- асинхронную функцию, которая запустится X раз
- функция должна считать от 0 до числа X
- между выводом чисел должны быть паузы по 0,5 сек
"""
import asyncio


async def print_counter(x: int):
    for number in range(x):
        print(number)
        await asyncio.sleep(.5)

async def start(x: int):
    coroutines = []
    for _ in range(x):
        coroutines.append(
            asyncio.create_task(print_counter(x))
        )

    await asyncio.wait(coroutines)

#print(print_counter(x))

#print_counter(5)

#start(2)
user_count = int(input("Count of functions >>> "))
asyncio.run(start(user_count))

