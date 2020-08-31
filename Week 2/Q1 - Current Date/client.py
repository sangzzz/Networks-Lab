import socket as S

try:
    s = S.socket(S.AF_INET, S.SOCK_STREAM)
    print("Client Created Successfully")
except:
    print("Client Creation Failed")


port = 3000
host = S.gethostname()

s.connect((host, port))

print(s.recv(1024))
s.send(bytes("Get Date.", "utf-8"))
date = s.recv(1024)

print("Today's Date : " + str(date))
s.close()
