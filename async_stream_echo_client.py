import asyncio

port = 2500
BUFSIZE = 1024

async def main():
    reader, writer = await asyncio.open_connection('localhost', port)

    while True:
        data = input()
        writer.write(data.encode())
        await writer.drain()

        data = await reader.read(BUFSIZE)
        print(data.decode())

asyncio.run(main())
