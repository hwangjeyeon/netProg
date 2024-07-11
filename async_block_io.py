import asyncio, time

def blocking_id():
    print(time.strftime('%X'))
    time.sleep(1)


async def main():
    await asyncio.gather(asyncio.to_thread(blocking_id), asyncio.sleep(1))

asyncio.run(main())