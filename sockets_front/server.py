import asyncio, time

async def handle_echo(reader, writer):
    # while True:
        # data = await reader.read(100)
        # message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"New conecction from {addr!r}")

    # data = await reader.read(100000)
    # message = data.decode()
    # print(f"Received {message} from {addr!r}")

    while True:
        message = input('Enviar al cliente: > ')
        print(f"Send: {message!r}")
        writer.write(message.encode())
        await writer.drain()

        # print('Se lanza el for')
        # for i in range(10):
        #     print(f"Sending {i} to {addr!r}")
        #     writer.write(str(i).encode())
        #     await writer.drain()
        #     await asyncio.sleep(2)

        # message = 'holaaa'
        # data = message.encode()

        # print(f"Send: {message!r}")
        # writer.write(data)
        # await writer.drain()

        # print("Close the connection")
        # writer.close()

host = '127.0.0.1'
port = 1234
async def main():
    server = await asyncio.start_server(
        handle_echo,
        host,
        port
    )

    print(f'Lanzando el server...')
    await server.serve_forever()

asyncio.run(main())