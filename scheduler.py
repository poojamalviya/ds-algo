
from elevator import Elevator

class Scheduler:
    def __init__(self):
        # self.up = set()
        # self.down = set()
        self.elev = Elevator()
        # self.state = Elevator().state
        # self.dir = Elevator().dir
    
    def request(self, currentFloor, requestedFloor):
        if(currentFloor < requestedFloor):
            self.elev.up.add(currentFloor)
            self.elev.up.add(requestedFloor)
            print self.elev.up
            
        else:
            self.elev.down.add(currentFloor)
            self.elev.down.add(requestedFloor)


s = Scheduler()
s.request(0,7)

