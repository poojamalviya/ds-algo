import random 
import Cookie
c = Cookie.SimpleCookie()
from pickle import dump, load

class Event:
    def __init__(self, data):
        self.id = data.get('id')
        self.type = data.get('type')
        self.title = data.get('title')
        self.start = data.get('start')
        self.end = data.get('end')
        self.location =data.get('location')
        self.owner = data.get('owner')
        self.userList = data.get('userList')
    
    def create(self):
        f = open('stor.json', 'w')
        dump(dict(evn =self.id), f)
        return "saved!"

    def get(self):
        return c[self.id]


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def create(self):
        json.dumps(dictionary, indent = 4) 
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
        return "saved!"
    
    def get(self):
        return c[self.id]

class EventCreator:
    def __init__(self, id, creatorName, userList):
        self.id = id
        self.creatorName = creatorName
        # self.userList = 

class Status:
    def __init__(self, state):
        self.state = enumerate('ACCEPT', 'DECLINE', 'NEUTRAL')



def createEvent(data):
    event = {}
    event['id'] = str(random.randint(1, 101))
    event['title'] = data.get('title'),
    event['type'] = data.get('type'),
    event['start'] = data.get('start'),
    event['end'] = data.get('end'),
    event['location'] = data.get('location'),
    event['userList'] = data.get('userList'),
    event['owner'] = data.get('owner')
    e = Event(event)
    return e.save()


def creatUser(name):
    user = {}
    user['id'] = str(random.randint(1, 101))
    user['name'] = name
    u = Event(user)
    print user.get('id')
    return u.create()

edata = {
    'type' : "calendar invite",
    'start' : "9:00 pm",
    'end' : '10:00 pm',
    'location' : '"bangalore',
    'userList' : ["Nish", 'Neha'],
    'title' : "Bug report"
}

creatUser("pooja")

# createEvent(edata)
# f = open('stor.bin', 'r')
# a =  load(f)
# print hasattr(a, '__name__')
# print a.get('id')


