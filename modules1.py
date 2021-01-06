import socket

def ports():
    x =  input("Enter The Ip: ")
    y = int(input("Enter The Port: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect_ex((x, y))

    if s.connect_ex((x, y)) != 0:
        print("This port is open")
    else:
        print("This port isnt open.")


