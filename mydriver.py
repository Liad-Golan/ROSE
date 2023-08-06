from rose.common import obstacles, actions  # NOQA

driver_name = "Itay(?)"

find2 = True
vision = []

def worthcheck(world):
    return False

def drive(world):
    global find2
    global home
    global vision
    if find2:
        find2 = False
        home = (world.car.x,world.car.y)
    pos = (world.car.x,world.car.y)
    for i in range(3):
        list = []
        for j in range(1+2*(i+1)):
            if (pos[0]-i+j>0) and (pos[0]-i+j<5):
                list.append(world.get((pos[0]-i+j,pos[1]+i)))
            else:
                list.append("B")
        vision.append(list)

    worth = worthcheck(world)
    if worth:
        pass
    else: #what to do if there isn't a worthy prize in sight(deafult)
        if vision[0][1] == obstacles.BARRIER or vision[0][1] == obstacles.BIKE or vision[0][1] == obstacles.TRASH or vision[0][1] == obstacles.CRACK or vision[0][1] == obstacles.WATER:
            if vision[0][0] == obstacles.NONE:
                return actions.LEFT
            elif vision[0][2] == obstacles.NONE:
                return  actions.RIGHT
        if pos[0] < home[0]:
            return actions.RIGHT
        if pos[0] > home[0]:
            return actions.LEFT
    return actions.NONE

