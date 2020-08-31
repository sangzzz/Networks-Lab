import socket as S

try:
    s = S.socket(S.AF_INET, S.SOCK_STREAM)
    print("Client Created Successfully")
except:
    print("Client Creation Failed")


port = 3000
host = S.gethostname()

s.connect((host, port))

while True:
    x = input("Client's Message : ")
    s.send(bytes(x, "utf-8"))
    y = str(s.recv(1024))
    if y[2:-1] == "Close":
        break
    print("Server Response : " + y)

print("Chat Closed")

s.close()
