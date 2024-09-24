# листинг 2.7
#->int задаем тип int (потому что питон - безтиповый язык)
#f важен, без него он не воспримет как переменную
#Далее создаем 3 задачи в питоне
#await - стартуем функции. Задачи запустились и выполняются одновременно - выполнится та, что занимает меньше времени

import asyncio

async def delay(delay_second: int)-> int:
    print(f'засыпаю на {delay_second} c')
    await asyncio.sleep(delay_second)
    print(f'сон в течение{delay_second} c закончился')
    return delay_second

async def add_one(number: int) -> int: #чистый калькулятор - питон тратит все силы на счет, поэтому может не переключиться на нужные задачи
    return number + 1

async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'

async def main() -> None:
    message = await hello_world_message() #запускаются параллельно эти 2 команды, то есть hello world выполняется быстрее
    one_plus_one = await add_one(1)
    print(one_plus_one) #но выводятся в порядке, что мы установим
    print(message)

asyncio.run(main()) #для параллельного запуска, без нее запуск будет последовательным

#python CW2409.py - запуск кода на в гитхабе
#