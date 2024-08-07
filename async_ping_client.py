import asyncio

async def ping_client():
    reader, writer = await asyncio.open_connection(host='localhost', port=8000)

    for _ in range(10):
        writer.write(b'ping')

        data = await reader.read(8)
        print(data.decode())
        await asyncio.sleep(1)
    
    writer.write(b'done')
    print('send: ping')
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    asyncio.run(ping_client())