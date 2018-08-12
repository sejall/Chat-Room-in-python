import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

uname = input("Enter user name!")
port=int(input("Enter 4 digit password assigned to you!"))
s.connect(("127.0.1.1", port))
s.send(uname.encode('ascii'))

clientRunning = True

def receiveMsg(sock):
    serverDown = False
    while clientRunning and (not serverDown):
        try:
            msg = sock.recv(1024).decode('ascii')
            print(msg)
        except:
            print('Server is Down. You are now Disconnected. Press enter to exit...')
            serverDown = True


threading.Thread(target = receiveMsg, args = (s,)).start()
while clientRunning:
    tempMsg = input()
    msg = uname + '>>' + tempMsg
    if 'quit' in msg:
        clientRunning = False
        s.send('quit'.encode('ascii'))
    else:
        s.send(msg.encode('ascii'))
