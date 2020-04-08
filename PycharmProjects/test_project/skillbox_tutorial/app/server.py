#
# Серверное приложение для соединений
#

import asyncio
from asyncio import transports
from typing import Optional, Mapping, Any


class ServerProtocol(asyncio.Protocol):
    login: str = None
    server: 'Server'
    transport: transports.Transport
    login_list: list = []
    message_history: list = []

    def __init__(self, server: 'Server'):
        self.server = server

    def send_history(self):
        for message in self.message_history[-10:len(self.message_history)]:
            self.transport.write(f">> {message}".encode())

    def data_received(self, data: bytes):

        decoded = data.decode()

        if self.login is not None:
            self.send_message(decoded)
        else:
            if decoded.startswith("login:"):
                self.login = decoded.replace("login:", "").replace("\r\n","")
                # проверка, что такого логина еще нет
                if self.login in self.login_list:
                    self.transport.write(
                        f"Логин {self.login} занят, попробуйте другой!\n".encode()
                    )
                    self.transport.close()
                else:
                    self.login_list.append(self.login)
                    self.transport.write(
                        f"Привет, {self.login}!\n".encode()
                    )
                    self.send_history()
            else:
                self.transport.write("Некорректный login\n".encode())

    def connection_made(self, transport: transports.Transport):
        self.server.clients.append(self)
        self.transport = transport

        print("Появился новый клиент")

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print(f"Клиент {self.login} отсоеденился")

    def send_message(self, content: str):
        message = f"<{self.login}>: {content}"
        self.message_history.append(message)

        for user in self.server.clients:
            user.transport.write(message.encode())



class Server:
    clients: list

    def __init__(self):
        self.clients = []

    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.build_protocol,
            '127.0.0.1',
            8888
        )

        print("Сервер запущен ... ")

        await coroutine.serve_forever()

process = Server()

try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")
