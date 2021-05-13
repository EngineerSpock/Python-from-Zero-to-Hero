import asyncio


async def tick():
    print("Tick")
    await asyncio.sleep(1)
    print("Tock")
    return 'Tick-Tock'


async def main():
    t1 = asyncio.create_task(tick(), name='tick1')
    t2 = asyncio.ensure_future(tick())

    # await t1
    # await t2

    results = await asyncio.gather(t1, t2)

    print(f'{t1.get_name()}. Done = {t1.done()}')
    print(f'{t2.get_name()}. Done = {t2.done()}')

    for x in results:
        print(x)


if __name__ == '__main__':
    asyncio.run(main())
