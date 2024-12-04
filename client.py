import socket
from D_H import KeyBox

class TcpClient:
    def __init__(self, port):
        self.key = KeyBox()
        self.socket_client = socket.socket()
        self.connect(port)

    def connect(self, port):
        self.socket_client.connect(("localhost", port))
        print('连接成功')
        
        send_msg = str(self.key.get_public_key())
        # 发送消息
        self.socket_client.send(send_msg.encode("UTF-8"))
        # 接受消息
        recv_data = self.socket_client.recv(1024).decode("UTF-8")    # 1024是缓冲区大小，一般就填1024， recv是阻塞式
        print(f"对方发来的公钥是：{recv_data}")
        data = int(recv_data)
    
        # 计算密钥
        key = self.key.get_key(data)
        print(f'获取密码为: {key}')

        # 关闭连接
        self.socket_client.close()

        

if __name__ == '__main__':
    usr2 = TcpClient(8887)