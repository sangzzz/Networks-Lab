import socket as S
from datetime import datetime
try:
    s = S.socket(S.AF_INET, S.SOCK_STREAM)
    print("Socket Created Successfully!!")
except:
    print("Socket Creation Failed!!")

host = S.gethostname()
port = 3000

s.bind((host, port))

s.listen(10)

c, address = s.accept()
print("Got Connection From : " + str(address))
# c.send(bytes("Connection Established", "utf-8"))

while True:
    print("Client Message : " + str(c.recv(1024)))
    x = input("Server's Response : ")
    c.send(bytes(x, "utf-8"))
    if x == "Close":
        break

print("Chat Application Closed")
c.close()
s.close()
