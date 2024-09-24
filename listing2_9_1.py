import asyncio

async def delay(delay_second: int)-> int:
    print(f'засыпаю на {delay_second} c')
    await asyncio.sleep(delay_second)
    print(f'сон в течение{delay_second} c закончился')
    return delay_second

async def main():
    sleep_for_three = asyncio.create_task(delay(19))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(8))

    await sleep_for_three
    await sleep_again
    await sleep_once_more


#Другой способ (осознать этот способ - тут можно ввести 1000)
async def main(): #async - помещает внутрь декоратора
    xs=[asyncio.create_task(delay(x)) for x in range(10)]
    for x in xs:
        await x #необходимо вставить, чтобы он начинал следующую процедуру
asyncio.run(main())

#Тут будут сильнее задержки из-за квадрата
async def main():
    xs=[asyncio.create_task(delay(x*x)) for x in range(10)] #тут будут сильнее задержки
    for x in xs:
        await x #необходимо вставить, чтобы он начинал следующую процедуру
asyncio.run(main())

# 2.16 - декоратор