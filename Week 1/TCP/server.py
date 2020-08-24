import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("SOCK_STREAM Socket Created Successfully!!")
except:
    print("Socket creation failed...")

port = 3000
host = socket.gethostname()
s.bind((host, port))


# Listen for connections....
s.listen(10)

while True:
    c, address = s.accept()
    print("Got connection from " + str(address))
    c.send(bytes("Connection Established!", 'utf-8'))
    print(c.recv(1024))
    # 1024 is the packet size
    c.close()
