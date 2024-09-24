import asyncio

async def delay(delay_second: int)-> int:
    print(f'засыпаю на {delay_second} c')
    await asyncio.sleep(delay_second)
    print(f'сон в течение{delay_second} c закончился')
    return delay_second


async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_once_more

asyncio.run(main())

async def main():
    sleep_for_three = asyncio.create_task(delay(19))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(8))

    await sleep_for_three
    await sleep_again
    await sleep_once_more

asyncio.run(main())