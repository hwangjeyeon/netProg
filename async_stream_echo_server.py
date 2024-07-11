import asyncio

port = 2500
BUFFSIZE = 1024


async def handle_echo(reader, writer):
    while True:
        data = await reader.read(BUFFSIZE)
        addr = writer.get_extra_info('peername')

        writer.write(data)
        await writer.drain()
    
async def main():
    server = await asyncio.start_server(handle_echo, '', port)

    addr = server.sockets[0].getsockname()

    await server.serve_forever()

asyncio.run(main())