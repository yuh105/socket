# -*- coding:utf-8 -*-
import socket

def server_init():
    host = "localhost" # your hostname
    port = 5000

    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversock.bind((host,port))
    serversock.listen(5)

    return serversock

def server_session_loop(serversock):
    clientsock, (client_address,client_port) = serversock.accept()
    print("Conneted by {0}".format(str(client_address)))
    while True:
        receive_message = clientsock.recv(1024).decode('utf-8')
        if receive_message == 'quit':
            break
        print('{0} : {1}'.format(client_address,receive_message))
    clientsock.close()


def main():
    serversock = server_init()
    print('Waiting for connections...')

    server_session_loop(serversock)



if __name__ == '__main__':
    main()