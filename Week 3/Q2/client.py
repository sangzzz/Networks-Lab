import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Client Socket Creation Successful!")
except:
    print("Client Socket Creation Failed!")

print()
host = socket.gethostname()
port = 3000

s.connect((host, port))

print("To close the connection, enter '!!'")
print("Enter strings.\n")

while True:
    req = input("Message to Server : ")
    s.send(bytes(req, "utf-8"))
    if req == '!!':
        break

print()
choice = input(s.recv(1024).decode("utf-8") + " : ")
s.send(bytes(choice, "utf-8"))
print(s.recv(1024).decode("utf-8"))

s.close()
