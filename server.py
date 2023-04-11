import ssl
import socket

tickets = 2

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="certi.pem")

hostPort = 1234
hostName = "127.0.0.1"

bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bindsocket.bind((hostName, hostPort))
bindsocket.listen(1)

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)

    data = connstream.recv(1024).decode()
    if(data=="d"):
        msg = str(tickets)
        connstream.send(str.encode(msg))
        #print("Display Request")
    elif(data=="b"):
        if(tickets>0):
            tickets -= 1
            connstream.send(str.encode("Successfully booked a ticket"))
        else:
            connstream.send(str.encode("Ticket could not be booked"))
        #print(tickets)
        #print("Book Request")