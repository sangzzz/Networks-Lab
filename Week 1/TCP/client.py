import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created Successfully!!")
except:
    print("Socket creation failed...")

port = 3000
host = socket.gethostname()
s.connect((host, port))

print(s.recv(1024))
s.send(bytes("Connected to server", 'utf-8'))
s.close()
