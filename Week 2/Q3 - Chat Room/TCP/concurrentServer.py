import socket
import threading
from _thread import *


lock = threading.Lock()


def threaded(c, thread_number):
    while True:
        req = c.recv(1024)
        print("Client-" + str(thread_number) +
              "s Message : " + str(req.decode("utf-8")))
        if not req:
            print("No Data Received!")
            break
        res = input("Server's Response to Client-" +
                    str(thread_number) + " : ")
        c.sendall(bytes(res, "utf-8"))

    c.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 3000

s.bind((host, port))

s.listen(5)
print("Server socket listening...")
thread_number = 0

while True:
    c, address = s.accept()

    print("Connected to : " + str(address[0]) + ' : ' + str(address[1]))
    thread_number += 1
    print("Thread Number : " + str(thread_number))
    start_new_thread(threaded, (c, thread_number))

s.close()
