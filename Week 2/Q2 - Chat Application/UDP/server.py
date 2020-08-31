import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("DGRAM Server Socket Created Successfully!")
except:
    print("DGRAM Socket Creation Failed!")

host = socket.gethostname()
port = 3000
client_port = 4000

s.bind((host, port))

while True:
    data, addr = s.recvfrom(1024)
    print("Client's Message : ", str(data.decode("utf-8")))
    x = input("Server's Response : ").strip()
    s.sendto(bytes(x, "utf-8"), (host, client_port))
    if x == "Close":
        break

print("Server Closed!!")
s.close()
