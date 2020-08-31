import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("DGRAM Client Socket Created Successfully!")
except:
    print("DGRAM Socket Creation Failed!")

host = socket.gethostname()
port = 4000
server_port = 3000

s.bind((host, port))

while True:
    s.sendto(bytes(input("Message To Server : ").strip(),
                   "utf-8"), (host, server_port))
    data, addr = s.recvfrom(1024)
    if bytes("Close", "utf-8") == data:
        break
    print("Server's Response : " + data.decode("utf-8"))

print("Client Signing off.")
s.close()
