from fbchat import Client
from fbchat.models import *
import json

path = 'grocery/list.txt'

def __loadCredential(app):
    with open('credentials/'+app+'.json', 'r') as f:
        credential = json.load(f)
    return credential

def load():
    with open(path, 'r') as f:
        list = f.read().splitlines()
    return list

def add(item):
    with open(path, 'a') as f:
        f.write(item)
        f.write('\n')

def reset():
    open(path, 'w').close()

def send():
    """
    This will use the facebook api to send the grocery list as a message to user
    """
    try:
        fb_credential = __loadCredential('fb')
        client = Client(fb_credential['email'], fb_credential['password'])
        grocery_list = load()
        message = "<Sent from A.I管家>\n\nYour Grocery List:\n- {}".format("\n- ".join(grocery_list))
        client.send(Message(text=message), thread_id=client.uid, thread_type=ThreadType.USER)
        client.logout()
        return True
    except:
        return False
    



