from rose.common import obstacles, actions  # NOQA

driver_name = "Itay(maybe good?)"
find2 = True
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
            if (pos[0]-i+j>=0) and (pos[0]-i+j<=5):
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

        #does what it must
        if (vision[0][1] != obstacles.NONE):
            if (vision[0][0] != obstacles.NONE and vision[0][0] != obstacles.PENGUIN):
                return actions.RIGHT
            elif vision[0][2] != obstacles.NONE and vision[0][2] != obstacles.PENGUIN:
                return actions.LEFT
        if (vision[0][0] != obstacles.NONE and vision[0][0] != obstacles.PENGUIN) and (vision[0][2] != obstacles.NONE and vision[0][2] != obstacles.PENGUIN):
            return actions.NONE
        best = -1
        obst = None
        found = False
        for i in range(3):
            for cur in GoodList:
                if vision[1][i+1] == cur and (vision[0][i] == obstacles.NONE or vision[0][i] == obstacles.PENGUIN):
                    found = True
                    best = i
                    obst = cur
                    if cur == GoodList[0]:
                        return ActionList[i]
                    break
            if found:
                break
        st = 0
        fin = 4
        act = [actions.LEFT,actions.NONE,actions.RIGHT]
        if (vision[0][0] != obstacles.PENGUIN and vision[0][0] != obstacles.NONE):
            st = 1
            act.remove(actions.LEFT)
        elif (vision[0][2] != obstacles.PENGUIN and vision[0][2] != obstacles.NONE):
            fin = 3
            act.remove(actions.RIGHT)
        for i in range(st,fin):
            for cur in GoodList:
                if obst != None:
                    if GoodList.index(obst) <= GoodList.index(cur):
                        break
                if vision[2][i+2] == cur:
                    if i == st or i == fin:
                        if (vision[1][i+1] == obstacles.NONE or vision[1][i+1] == obstacles.PENGUIN):
                            if i <= ((fin + st) / 2):
                                return act[0]
                            else:
                                return act[-1]
                    else:
                        print(i)
                        print(vision)
                        if (vision[1][i+1 ] in GoodList):
                            if (vision[0][i] == obstacles.NONE or vision[0][i] == obstacles.PENGUIN):
                                return ActionList[i]
                        else:
                            if (vision[1][i + 1] == obstacles.NONE or vision[1][i + 1] == obstacles.PENGUIN):
                                if i <= ((fin + st) / 2):
                                    return act[0]
                                else:
                                    return act[-1]
        if best != -1:
            return ActionList[best]
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