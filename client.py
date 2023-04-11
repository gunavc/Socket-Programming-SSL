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
    data = conn.recv(1024).decode()
    alert_label.config(text=data)
    
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

window = tk.Canvas(root,height=650, width=650)
window.pack()

#Displaying no. of available tickets
ticketDisplay = tk.Label(window, text="Tickets=",font=("Helvetica",20))
getTicket()
ticketDisplay.grid(row=0, column=1, padx=10, pady=30)

#Notice Label
nlabel = tk.Label(window, text="Click the button to book a ticket")
nlabel.grid(row=1,column=1)

#Button to book ticket
bookButton = tk.Button(window, text="Book Ticket", command= lambda : bookTicket())
bookButton.grid(row=2,column=1)

#Alert label
alert_label = tk.Label(window, text="")
alert_label.grid(row=3, column=1)

# Packing all the items
window.place()

root.geometry("500x300")
root.mainloop()