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

print("To close the connection, enter 'bye'")
print()

while True:
    req = input("Message to Server : ")
    s.send(bytes(req, "utf-8"))
    res = s.recv(1024).decode("utf-8")
    print("Server's Response : " + str(res))
    if res == "Bye":
        print("Client signing off.")
        break

s.close()
