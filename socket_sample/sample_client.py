# -*- coding:utf-8 -*-
import socket

def client_init():
    host = "localhost"  # your hostname
    port = 5000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    return client

def client_session_loop(client):
    print('input your message')
    while True:
        send_message = input('>> ')
        client.send(send_message.encode('utf-8'))
        if send_message == 'quit':
            break

def main():

    client = client_init()
    client_session_loop(client)


if __name__ == '__main__':
    main()