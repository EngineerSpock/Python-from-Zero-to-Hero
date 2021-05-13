import asyncio


class ErrorThatShouldCancelOtherTasks(Exception):
    pass


async def my_sleep(secs):
    print(f'task {secs}')
    await asyncio.sleep(secs)
    print(f'task {secs} finished sleeping')

    if secs == 5:
        raise ErrorThatShouldCancelOtherTasks('5 is forbidden')
    print(f'Slept for {secs} secs')


async def main_cancel_tasks():
    tasks = [asyncio.create_task(my_sleep(secs)) for secs in [2, 5, 7]]
    sleepers = asyncio.gather(*tasks)
    print('awaiting')
    try:
        await sleepers
    except ErrorThatShouldCancelOtherTasks:
        print('Fatal error. Cancelling...')
        for t in tasks:
            print(f'cancelling {t}')
            print(t.cancel())
    finally:
        await asyncio.sleep(5)


async def main_cancel_future():
    sleepers = asyncio.gather(*[my_sleep(secs) for secs in [2, 5, 7]])
    print('awaiting')
    try:
        await sleepers
    except ErrorThatShouldCancelOtherTasks:
        print('Fatal error. Cancelling...')
        sleepers.cancel()
    finally:
        await asyncio.sleep(5)


if __name__ == '__main__':
    asyncio.run(main_cancel_tasks())
    # asyncio.run(main_cancel_future())
