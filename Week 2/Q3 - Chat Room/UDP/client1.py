import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("DGRAM Client Creation Successful.")
except:
    print("DGRAM Clienr Creation Failed.")


host = socket.gethostname()
port = 4000

s.bind((host, port))

target = (host, 3000)

while True:
    req = input("Message to Concurrent Server : ")
    s.sendto(bytes(req, "utf-8"), target)
    res, address = s.recvfrom(1024)
    res = res.decode("utf-8")
    print("Server's Response : " + str(res))

s.close()
