import asyncio
import threading
import time


class Terminal:

    async def start(self):
        loop = asyncio.get_running_loop()
        future = loop.create_future()

        t = threading.Thread(target=self.run_cmd, args=(loop, future,))
        t.start()

        return await future

    def run_cmd(self, loop, future):
        time.sleep(3)
        loop.call_soon_threadsafe(future.set_result, 1)


async def main():
    t = Terminal()
    result = await t.start()
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
