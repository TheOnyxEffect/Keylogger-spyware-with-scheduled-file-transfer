import socket

s= socket.socket()
#host= input(str("Enter address of sender: "))
host= "ONYX-PC"

port= 8080
s.connect((host, port))
print("connected...")

filename = "received_file.txt"
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File received successfully")