from rose.common import obstacles, actions  # NOQA

driver_name = "Itay(?)"

find2 = True
goal = False
GoodList = [obstacles.PENGUIN,obstacles.CRACK,obstacles.WATER] #obstacles that earn points
ActionList = [actions.LEFT,actions.NONE,actions.RIGHT]
def worthcheck(world):
    return False

def drive(world):
    global find2
    global home
    vision = []
    if find2:
        find2 = False
        home = (world.car.x,world.car.y)
    pos = (world.car.x,world.car.y)
    #"scanns"
    for i in range(1,4): # i = line we're checking
        list = []
        for j in range(1+2*(i)): #j = square in line we're cheking
            if (pos[0]-i+j>0) and (pos[0]-i+j<5):
                list.append(world.get((pos[0]-i+j,pos[1]-i)))
            else:
                list.append("B")
        vision.append(list) #  vision = list of all the obstacles in front of us
    #add a worthy path finder
    worth = worthcheck(world)
    if worth:
        pass
    else: #what to do if there isn't a worthy prize in sight(deafult)
        #point greedy
        if vision[0][1] == obstacles.PENGUIN:
            return actions.PICKUP
        if vision[0][1] == obstacles.CRACK:
            return actions.JUMP
        if vision[0][1] == obstacles.WATER:
            return actions.BRAKE

        best = 1
        obst = None
        for i in range(3):
            for cur in GoodList:
                if vision[1][i+1] == cur and (vision[0][i] == obstacles.NONE or vision[0][i] == obstacles.PENGUIN):
                    best = i
                    obst = cur
                    if cur == GoodList[0]:
                        return ActionList[i]




        #what he does if there is an obstacle in front of him.
        if vision[0][1] != obstacles.NONE:
            if vision[0][0] == obstacles.NONE:
                return actions.LEFT
            elif vision[0][2] == obstacles.NONE:
                return  actions.RIGHT
        # else.
        if pos[0] < home[0] and vision[0][2] == obstacles.NONE:
            return actions.RIGHT
        if pos[0] > home[0] and vision[0][0] == obstacles.NONE:
            return actions.LEFT
    return actions.NONE

#python rose-client -s 128.52.61.161 mydriver.py