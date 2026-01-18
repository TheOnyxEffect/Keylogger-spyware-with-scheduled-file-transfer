import socket
import os

s= socket.socket()
host= socket.gethostname()
port= 8080
s.bind((host, port))
s.listen(1)
print("host: ", host)
print("waiting for connection")
conn, addr= s.accept()
print(addr, "connected to the server")

filename = "transfer_file.txt"
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("File sent successfully")
file.close()
os.remove("transfer_file.txt")
