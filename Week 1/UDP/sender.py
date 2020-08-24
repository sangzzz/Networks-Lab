import socket

UDP_IP = socket.gethostname()
UDP_PORT = 8000

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("DATAGRAM CLIENT CREATED SUCCESSFULLY")
except:
    print("SOCKET CREATION FAILED")
s.bind((UDP_IP, UDP_PORT))

while True:
    # buffer size is 1024 bytes
    data, addr = s.recvfrom(1024)
    print(data)
