import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server Socket Creation Successful!")
except:
    print("Server Socket Creation Failed!")

print()
host = socket.gethostname()
port = 3000

s.bind((host, port))
s.listen(5)

c, address = s.accept()
while True:
    string = c.recv(1024).decode("utf-8")
    print("Client's Request : " + str(string))
    if string == "Bye":
        c.send(bytes("Bye", "utf-8"))
        break
    else:
        c.send(bytes(string.upper(), "utf-8"))
c.close()
print("Client has closed the connection")

# print("Server Closed!")
s.close()
