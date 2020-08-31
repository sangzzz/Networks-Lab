import socket


def myfunc(e):
    return len(e)


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
strings = []
while True:
    string = c.recv(1024).decode("utf-8")
    print("Client's Request : " + str(string))
    if string == "!!":
        break
    else:
        strings.append(string)


c.send(bytes(
    "\t\tMENU\n1. Sort by length\n2. Sort alphabetically\nEnter Your Choice[1/2]", "utf-8"))
choice = c.recv(1024).decode("utf-8")

if choice == '1':
    strings.sort(key=myfunc)
elif choice == '2':
    strings.sort()

c.send(bytes("Sorted strings : " + str(strings), "utf-8"))
c.close()
print("Client has closed the connection")
s.close()
