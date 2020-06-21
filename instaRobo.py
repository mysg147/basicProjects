from instapy import InstaPy
import getpass
import instaloader

class Roboinsta:
    def __init__(self, userName,passWord):
        self.userName=userName
        self.passWord=passWord

    def sessionBy_py(self):
        session = InstaPy(username= self.userName, password=self.passWord,headless_browser=True)
        return session

    def LBy_loader(self):
        L = instaloader.Instaloader()
        L.login(self.userName,self.passWord )  
        return L

#all of the accounts who do follow the user WHOM user itself also do follow back
def awwu(session,profileBy_session):
        mutual_following = session.pick_mutual_following(username=profileBy_session, live_match=True, store_locally=True)
        return mutual_following
#Accept all follow request
def accept_follow_requests(session):
    session.accept_follow_requests(amount=100, sleep_delay=1)

def createprofile(L,username):
    profile = instaloader.Profile.from_username(L.context, username)
    return profile

def options():
    k=("Menu :-\n"
        "1) Number of all of the accounts who do follow the user WHOM user itself also do follow back"
        "\n2) Acept all pending follow request"
        "\n3) Show the bio of particular account"
        "\n4) Download all the post of particular account"
        "\n5) Search"
        "\n6) Get profile pic URL"
        "\n7)get saved post"
        "\n8) Exit")
        
    print(k)
    k=input()
    return k


def main():
    userName=input("Enter username/Email/Phoneno:")
    passWord=getpass.getpass(prompt='Password:',stream=None)
    object1=Roboinsta(userName,passWord)
    session=object1.sessionBy_py()
    session.login()
    L=object1.LBy_loader()

    while(True):
        k=options()
        
        if k=='1':
            username1=input("Enter desired username:")
            mutual_following=awwu(session,username1)
            print(len(mutual_following))
            print("="*22)
            for i in mutual_following:
                print(i)
        if k=='2':
            accept_follow_requests(session)
        if k=='3':
            username1=input("Enter desired username:")
            profile=createprofile(L,username1)
            print(profile.biography)    
        if k=='4':
            username1=input("Enter desired username:")
            profile=createprofile(L,username1)
            for post in profile.get_posts():
                L.download_post(post, target=profile.username)   
        if k=='5':
            
            search=input("what you want to search:-")
            print("By:-\n1)Profiles\n2)Location\n3)Hashtag Strings\n4)Hashtags\n5)Prefixed_username")
            s=input("Enter your chice-")
            tsr=instaloader.TopSearchResults(L.context,search)
            
            if s=='1': q=tsr.get_profiles()
            if s=='2':q=tsr.get_locations()
            if s=='3':q=tsr.get_hastag_string()
            if s=='4':q=tsr.get_hashtags()
            if s=='5':q=tsr.get_prefixed_usernames()
            for i in q:
                print(i)

        if k=='6':
            username1=input("Enter desired username:")
            profile=createprofile(L,username1)
            print(profile.profile_pic_url)

        if k=='7':
            
            profile=createprofile(L,userName)
            savedPost=profile.get_saved_posts()
            for i in savedPost:
                L.download_post(i, target=profile.username)

        if k=='8':
            break    

main()
 