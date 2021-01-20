import time

class ElevatorSystem:
    def __init__(self):
        self.e1 = Elevator()
        self.e2 = Elevator()
        self.new_req = set()
    
    def checkNearest(self, cf, rf, direction):
        nearest = 0        
        if self.e1.dir =='UP' and self.e2.dir == 'UP' and direction == 'UP':
            if self.e1.state < cf and self.e2.state < cf:
                diff_e1 = cf-self.e1.state
                diff_e2 = cf-self.e2.state 
                if diff_e1<diff_e2:
                    nearest = 1
                    return nearest
                else:
                    nearest = 2
                    return nearest
            elif self.e1.state < cf:
                nearest = 1
                return nearest
            elif self.e2.state < cf:
                nearest = 2
                return nearest
        elif self.e1.dir == 'UP' and direction == 'UP' and self.e1.state < cf:
            nearest = 1
            return nearest
        else:
            nearest = 2
            return nearest


        if self.e1.dir =='DOWN' and self.e2.dir == 'DOWN' and direction == 'DOWN':
            if self.e1.state > cf and self.e2.state > cf:
                diff_e1 = elf.e1.state - cf
                diff_e2 = elf.e2.state - cf
                if diff_e1<diff_e2:
                    nearest = 1
                    return nearest
                else:
                    nearest= 2
                    return nearest
            elif self.e1.state > cf:
                nearest= 1
                return nearest
            elif self.e2.state > cf:
                nearest= 2
                return nearest
        elif self.e1.dir == 'DOWN' and direction == 'DOWN' and self.e1.state > cf:
            nearest= 1
            return nearest
        else:
            nearest= 2
            return nearest

    
    # all the request coming dynamically will be added to newRequest and but not implementing event system now as per time constraint 
    def allocateRequest(self, currentFloor, requestedFloor):
        direction = None

        if(cf < rf):
            direction = 'UP'    
        else:
            direction = 'DOWN'
        nearestElevator = checkNearest(currentFloor, requestedFloor, direction)

        if nearestElevator == 1:
            if direction == 'UP':
                self.e1.up.add(currentFloor)
                self.e1.up.add(requestedFloor)
            else:
                self.e1.down.add(currentFloor)
                self.e1.down.add(requestedFloor)
        else:
            if direction == 'UP':
                self.e2.up.add(currentFloor)
                self.e2.up.add(requestedFloor)
            else:
                self.e2.down.add(currentFloor)
                self.e2.down.add(requestedFloor)

class Elevator:
    def __init__(self):
        self.state = 0
        self.up = set()
        self.down = set()
        self.dir = ('UP', 'DOWN', 'IDLE')

    def startElevator(self):
        if self.state == 0 and len(self.up)>0:
            self.moveUp()
        if len(self.down) > 0:
            self.moveDown()

    def moveUp(self): 
        while self.up:
            self.state = self.up.pop()
            self.dir = 'UP'
            time.sleep(1)
            print "Floor: ", str(self.state)

    def moveDown(self):
        for i in sorted(list(self.down), reverse=True):
            self.state = i
            self.dir = 'DOWN'
            time.sleep(1)
            print "Floor: ", str(self.state)
            self.down.remove(i)

            




# ele = Elevator()
# ele.request(0, 2)
# ele.request(0, 5)
# ele.request(6, 8)
# ele.request(2, 4)
# ele.request(3, 4)
# ele.request(9, 10)
# ele.request(11, 12)
# ele.request(7,2)
# ele.request(8,1)
# ele.request(4,2)
# ele.startElevator()

# ele = ElevatorSystem()
# ele.e1.state = 2
# ele.e1.dir = "DOWN"
# ele.e2.state = 2
# ele.e2.dir = "UP"
# print ele.checkNearest(4, 6)

while(True):
    e = ElevatorSystem()
    print('Enter your current floor and destination floor or press enter')
    currentFloor = input()

    time.sleep(1)
