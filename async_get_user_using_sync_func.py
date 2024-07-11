import asyncio, time

async def get_user(name):
    await asyncio.to_thread(time.sleep, 1)

async def main():
    start = time.time()
    await asyncio.gather(get_user('hwang'))
    end = time.time()


asyncio.run(main())