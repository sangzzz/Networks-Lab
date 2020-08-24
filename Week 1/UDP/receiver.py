import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("SOCK_DGRAM Socket Created Successfully!!")
except:
    print("Socket creation failed...")

port = 8000
host = socket.gethostname()


s.sendto(bytes("SENT FROM SERVER PORT 8000", 'utf-8'), (host, port))
