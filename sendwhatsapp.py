import pywhatkit as kit

def respond(c):
    if c=='1':
        #send message at particular time
        kit.sendwhatmsg("+9198********","testing done",19,52)

    if c=='2':
        #send particular file at particular time
        kit.send_file("+9198********","Path to file",15,00)

    if c=='3':
        #Will send message with most of the processes hidden
        kit.sendwhatmsg_with_selenium("+9198********","This is a message",15,00)

    if c=='4':
        #Will perform a Google search
        kit.search("Python")


    if c=='5':
        #Will show information of all the messages sent using this library
        kit.showHistory()

    if c=='6':
        exit()

def menu():
    print("1) send message\n2) send file\n3) send with selenium\n4) search\n5) show history\n6) Quit\n Enter your choice:-")
    respond(input())

def main():
    while True:
        menu()

main()