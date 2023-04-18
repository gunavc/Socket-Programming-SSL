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

    no_ticket = "1"
    if(ticket_entry.get()!=""):
        no_ticket = ticket_entry.get()

    req_msg = no_ticket
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
    ticketDisplay.config(text=data)
    conn.close()

#GUI
root = tk.Tk()

root.title("Ticket Booking System")
root.geometry("800x500")

header_label = tk.Label(root, text="Ticket Booking System", font=("Arial", 30), pady=20)
header_label.pack()

frame = tk.Frame(root)
frame.pack()

#Displaying no. of available tickets
ticket_label = tk.Label(frame, text="Available Tickets", font=("Arial", 20))
ticket_label.grid(row=0, column=0, padx=10, pady=30)

ticketDisplay = tk.Label(frame, text="", font=("Arial", 20))
getTicket()
ticketDisplay.grid(row=0, column=1, padx=10, pady=30)

#Notice Label
nlabel = tk.Label(frame, text="Enter the number of tickets to be booked", font=("Arial", 20))
nlabel.grid(row=1, column=0, pady=20)

#Input box to enter the  number of tickets
ticket_entry = tk.Entry(frame, width=10, font=("Arial", 20))
ticket_entry.focus_set()
ticket_entry.grid(row=1, column=1)

#Button to book ticket
bookButton = tk.Button(frame, text="Book Ticket", font=("Arial", 20), command= lambda : bookTicket())
bookButton.grid(row=2, column=1, pady=20)

#Alert label
alert_label = tk.Label(frame, text="", font=("Arial", 20))
alert_label.grid(row=3, column=1, pady=20)

root.mainloop()
