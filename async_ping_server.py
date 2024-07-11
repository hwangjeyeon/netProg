import asyncio

async def handle_asyncclient(reader, writer):
    print(writer.get_extra_info('peername'))
    while True:
        data = await reader.read(0)
        if data == b'ping':
            writer.write(b'ping')
            await writer.drain()
        elif data == b'done':
            break
        elif len(data) == 0:
            break
    writer.close()
    await writer.wait_closed()

async def server_asytncmain():
    server = await asyncio.start_server(handle_asyncclient, 'localhost', 8000)
    await server.serve_forever

if __name__ == '__main__':
    asyncio.run(server_asytncmain())
