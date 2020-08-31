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

while True:
    c, address = s.accept()
    print("Got Connection From : " + str(address))
    c.send(bytes("Connection Established", "utf-8"))
    print(c.recv(1024))
    c.send(bytes(str(datetime.now()), "utf-8"))
    c.close()
