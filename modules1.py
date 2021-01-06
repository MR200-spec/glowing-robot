import socket

def ports(host, port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect_ex((host, port))

    if s.connect_ex((host, port)) != 0:
        print("This port is open")
    else:
        print("This port isnt open.")



