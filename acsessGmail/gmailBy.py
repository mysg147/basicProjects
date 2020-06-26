import ezgmail


def respose(choice):
    if choice=='1':
        print("enter recipient:- ")
        recipient=input()
        subject=input("Enter subject:-")
        text=input("Enter your message(should be 1 liner):- ")
        #for i in range(0,len(recipients)):
         #   recipient=str(recipients[i])
        ezgmail.send(recipient,subject,text)

    if choice=='2':
        unread=ezgmail.unread()
        #get subject and date
        results=ezgmail.summary(unread)
        #print the email
        print(str(unread[0].messages[0]))

    if choice=='3':
        #searching
        gSearch=input("what you want to search:-")
        search_result=ezgmail.search(gSearch)
        print(len(search_result))
        results=ezgmail.summary(search_result)

    if choice=='4':
        #downloadinng
        gSearch=input("what you want to search:-")
        attacmentName=input("name of the attachment:-")
        download=ezgmail.search(gSearch)
        download[0].messages[0].downloadAttachment(attacmentName)

    if choice=='5':
        exit()

def options():
    print("what you want to do on gmail:-\n"
    "1) send mails\n"
    "2) unread messages\n"
    "3) search mail\n"
    "4) Download attachment from main\n"
    "5) exit")

def main():
    while True:
        options()
        choice=input()
        respose(choice)

main()