import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("STREAM socket creation success")
except:
    print("Socket creation failed!!")
    sys.exit()

host = socket.gethostname()
port = 3000

s.connect((host, port))


while True:
    req = input("Message to concurrent server : ")
    s.send(bytes(req, "utf-8"))
    res = s.recv(1024).decode("utf-8")
    print("Server's Response : " + str(res))

s.close()
