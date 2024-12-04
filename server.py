import socket
from D_H import KeyBox

class TcpServer:
    def __init__(self, port):
        self.key = KeyBox()

        self.port = port
        self.socket_server = socket.socket()
        self.socket_server.bind(("localhost", port))
        self.start()

    def start(self):
        self.socket_server.listen(1)
        conn, address = self.socket_server.accept()
        print('连接成功')


        # 接收消息
        data: str = conn.recv(1024).decode("UTF-8")
        print(f"对方发来的公钥是：{data}")
        data  = int(data)
        # 回复消息
        msg = str(self.key.get_public_key())
        conn.send(msg.encode("UTF-8"))

        # 计算密钥
        key = self.key.get_key(data)
        print(f'获取密码为: {key}')

        # 关闭连接
        conn.close()
        self.socket_server.close()
        

if __name__ == '__main__':
    user1 = TcpServer(8887)