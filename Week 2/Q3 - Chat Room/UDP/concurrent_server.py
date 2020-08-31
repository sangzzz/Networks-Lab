import socket
import threading
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 3000

s.bind((host, port))

print("Server socket listening...")

thread_number = 0
clients = {}
while True:
    req, address = s.recvfrom(1024)
    req = req.decode("utf-8")
    if address not in clients:
        thread_number += 1
        clients[address] = thread_number
    print("Thread Number : " + str(clients[address]))
    print("Client"+str(thread_number)+"'s Request : " + str(req))
    res = input("Response to Client"+str(thread_number)+" : ")
    s.sendto(bytes(res, "utf-8"), address)
    print()
s.close()
