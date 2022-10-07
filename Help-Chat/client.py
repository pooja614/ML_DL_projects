import tkinter as tk
from tkinter import messagebox
import socket
import threading
import webbrowser

window = tk.Tk()
window.title("Client")
username = " "


topFrame = tk.Frame(window,background="#fc032c")
lblName = tk.Label(topFrame, text = "Name:").pack(side=tk.LEFT)
entName = tk.Entry(topFrame)
entName.pack(side=tk.LEFT)
btnConnect = tk.Button(topFrame, text="Connect", command=lambda : connect())
btnConnect.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP)



displayFrame = tk.Frame(window,background="#fc032c")
lblLine = tk.Label(displayFrame, text="__________________________________________________________").pack()
scrollBar = tk.Scrollbar(displayFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(displayFrame, height=20, width=55)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
tkDisplay.tag_config("tag_your_message", foreground="#ffffff")
scrollBar.config(command=tkDisplay.yview,background="#a09f9f")
tkDisplay.config(yscrollcommand=scrollBar.set,foreground="#ffffff", background="#010318", highlightbackground="#fc032c",highlightthickness=4,state="disabled")
displayFrame.pack(side=tk.TOP)

def to_hyperlink(x):
    linkFrame=tk.Frame(window)
    clickName = tk.Label(linkFrame, text=x, fg="blue", cursor="hand2")
    clickName.pack()
    clickName.bind("<Button-1>", lambda event: webbrowser.open(clickName.cget("text")))
    linkFrame.pack(side=tk.BOTTOM)
    print(x)

solutionFrame=tk.Frame(window)
lblsol=tk.Label(solutionFrame, text="Above links might be helpful").pack()
tkADisplay=tk.Text(solutionFrame, height=1, width=55)
tkADisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5,0))
solutionFrame.pack(side=tk.BOTTOM, pady=(5,12))




bottomFrame = tk.Frame(window,background="#fc032c")
tkMessage = tk.Text(bottomFrame, height=2, width=55)
tkMessage.pack(side=tk.LEFT, padx=(5, 13), pady=(5, 10))
tkMessage.config(background="#f2484a",highlightbackground="grey", state="disabled")
tkMessage.bind("<Return>", lambda event: getChatMessage(tkMessage.get("1.0", tk.END)))
bottomFrame.pack(side=tk.BOTTOM)


def connect():
    global username, client
    if len(entName.get()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter your first name <e.g. John>")
    else:
        username = entName.get()
        connect_to_server(username)


# network client
client = None
HOST_ADDR ="127.0.0.1"
HOST_PORT = 8080

def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR
    # try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST_ADDR,HOST_PORT)) 
    client.send(name.encode()) # Send name to server after connecting

    entName.config(state=tk.DISABLED)
    btnConnect.config(state=tk.DISABLED)
    tkMessage.config(state=tk.NORMAL)

    # start a thread to keep receiving message from server
    # do not block the main thread :)
    threading._start_new_thread(receive_message_from_server, (client, "m"))


def receive_message_from_server(sck, m):
    while True:
        from_server = sck.recv(4096).decode()
        if not from_server: break
        
        if 'HAVE A LOOK AT THIS!!!' in from_server:
            source=from_server.split(">")[1]
            to_hyperlink(source)
            textl= tkADisplay.get("1.0", tk.END).strip()
            tkADisplay.config(state=tk.NORMAL)
            if len(textl) < 1:
                tkADisplay.insert(tk.END, to_hyperlink(from_server))
            else:
                tkADisplay.insert(tk.END, "\n\n"+ to_hyperlink(from_server))

            tkDisplay.config(state=tk.DISABLED)
            tkDisplay.see(tk.END)


        # display message from server on the chat window

        # enable the display area and insert the text and then disable.
        texts = tkDisplay.get("1.0", tk.END).strip()
        tkDisplay.config(state=tk.NORMAL)
        if len(texts) < 1:
            tkDisplay.insert(tk.END, from_server)
        else:
            tkDisplay.insert(tk.END, "\n\n"+ from_server)

        tkDisplay.config(state=tk.DISABLED)
        tkDisplay.see(tk.END)

        print("Server says: " +from_server)

    sck.close()
    window.destroy()


def getChatMessage(msg):

    msg = msg.replace('\n', '')
    texts = tkDisplay.get("1.0", tk.END).strip()

    # enable the display area and insert the text and then disable.
    tkDisplay.config(state=tk.NORMAL)
    if len(texts) < 1:
        tkDisplay.insert(tk.END, "You->" + msg, "tag_your_message") # no line
    else:
        tkDisplay.insert(tk.END, "\n\n" + "You->" + msg, "tag_your_message")

    tkDisplay.config(state=tk.DISABLED)

    send_mssage_to_server(msg)

    tkDisplay.see(tk.END)
    tkMessage.delete('1.0', tk.END)


def send_mssage_to_server(msg):
    client.send(msg.encode())
    if msg == "exit":
        client.close()
        window.destroy()
    print("Sending message")


window.mainloop()




