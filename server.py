#!/usr/bin/env python
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys, time

PORT_NUMBER = 5000
SIZE = 1024

def server():
    host_name = gethostbyname('0.0.0.0')
    my_socket = socket(AF_INET, SOCK_DGRAM)
    my_socket.bind((host_name, PORT_NUMBER))

    print("Test server listening on port {0}\n").format(PORT_NUMBER)
    
    try:
        while True:
            (data, addr) = my_socket.recvfrom(SIZE)
            print(data, addr)
    except KeyboardInterrupt:
        print("Server closed down by user") 
        sys.exit(0)
    except:
        print("Server error, closing down.")
        sys.exit(1)


if __name__ == '__main__':
    server()
   
