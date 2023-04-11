import ssl
import socket
import tkinter as tk


def bookTicket():
    context = ssl._create_unverified_context()
    serverPort = 1234
    serverName = "127.0.0.1"

    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Using TCP

    conn = context.wrap_socket(clientSocket,server_hostname=serverName)
    conn.connect((serverName, serverPort))

    req_msg = "b"
    conn.send(str.encode(req_msg))
    
    conn.close()
    getTicket()

def getTicket():
    context = ssl._create_unverified_context()
    serverPort = 1234
    serverName = "127.0.0.1"

    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Using TCP

    conn = context.wrap_socket(clientSocket,server_hostname=serverName)
    conn.connect((serverName, serverPort))

    req_msg = "d"
    conn.send(str.encode(req_msg))
    data = conn.recv(1024).decode()
    ticketDisplay.config(text=f"Available Tickets = {data}")
    conn.close()

# Writing the GUI
# Root window

root = tk.Tk()

Canvas = tk.Canvas(root,width=650, height=650)

#Displaying no. of available tickets
ticketDisplay = tk.Label(Canvas, text="Tickets=")
getTicket()


#Button to book ticket
bookButton = tk.Button(Canvas, text="Book Ticket", command= lambda : bookTicket())

# Packing all the items
Canvas.pack()
ticketDisplay.pack()
bookButton.pack()

root.mainloop()