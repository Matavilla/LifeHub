import socket
# create a socket object

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = "127.0.0.1"
port = 65534
print((host,port))
# connection to hostname on the port.
s.connect((host, port))
# Receive no more than 1024 bytes
msg = s.recv(1024)
s.close()
print (msg.decode('ascii'))