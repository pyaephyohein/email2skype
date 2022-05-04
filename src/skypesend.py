import os
from dotenv import load_dotenv
from skpy import Skype
load_dotenv()

def skype(text):
    username = os.getenv('skypeusername')
    password = os.getenv('skypepassword')
    receiver = os.getenv('receiver')
    # contact_type = os.getenv('contact_type')

    sk = Skype(username, password) # connect to Skype
    id = str(receiver)
    print(id)
    if id.startswith('live'):
        ch = sk.contacts[id].chat
        ch.sendMsg(text)
    elif id.startswith('19'):
        ch = sk.chats.chat(id)
        ch.sendMsg(text)
    else:
        print("contact type not supported")