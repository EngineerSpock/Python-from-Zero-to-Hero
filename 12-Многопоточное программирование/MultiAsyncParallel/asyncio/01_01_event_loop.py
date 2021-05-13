x = 'abc'

import asyncio
import time

from multithreading.decorators import measure_time, async_measure_time


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')

    loop = asyncio.get_running_loop()
    if loop.is_running():
        print('loop is still running')


async def main():
    awaitable_obj = asyncio.gather(tick(), tick(), tick())

    for task in asyncio.all_tasks():
        print(task, end='\n')

    await awaitable_obj


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()

        print('coroutines have finished')
    except KeyboardInterrupt:
        print('Manually closed application')
    finally:
        loop.close()
        print('loop is closed')
        print(f'loop is closed = {loop.is_closed()}')
