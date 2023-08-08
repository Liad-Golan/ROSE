from rose.common import obstacles, actions  # NOQA

driver_name = "Amir"




def drive(world):
    pls = 'M'
    harm = [obstacles.WATER, obstacles.CRACK, obstacles.TRASH, obstacles.BIKE, obstacles.BARRIER]
    bad_harm_water = [obstacles.TRASH, obstacles.BIKE, obstacles.BARRIER, obstacles.WATER]
    bad_harm_crack = [obstacles.TRASH, obstacles.BIKE, obstacles.BARRIER, obstacles.CRACK]
    not_harm = [obstacles.PENGUIN]
    x = world.car.x
    y = world.car.y
    if x == 0 or x == 3:
        pls = 'L'
    elif x == 2 or x == 5:
        pls = 'R'
    else:
        pls = 'M'
    # penguin chek:
    if pls == 'M':
        if world.get((x, y - 1)) == obstacles.PENGUIN:
            return actions.PICKUP
        if world.get((x - 1, y - 2)) == obstacles.PENGUIN and world.get((x - 1, y - 1)) not in harm:
            return actions.LEFT
        if world.get((x + 1, y - 2)) == obstacles.PENGUIN and world.get((x + 1, y - 1)) not in harm:
            return actions.RIGHT

    if pls == 'R':
        if world.get((x, y - 1)) == obstacles.PENGUIN:
            return actions.PICKUP
        if world.get((x - 1, y - 2)) == obstacles.PENGUIN and world.get((x - 1, y - 1)) not in harm:
            return actions.LEFT

    if pls == 'L':
        if world.get((x, y - 1)) == obstacles.PENGUIN:
            return actions.PICKUP
        if world.get((x + 1, y - 2)) == obstacles.PENGUIN and world.get((x + 1, y - 1)) not in harm:
            return actions.RIGHT

    # crack chek:
    if pls == 'M':
        if world.get((x, y - 1)) == obstacles.CRACK:
            return actions.JUMP
        if world.get((x - 1, y - 2)) == obstacles.CRACK and world.get((x - 1, y - 1)) not in bad_harm_water:
            return actions.LEFT
        if world.get((x + 1, y - 2)) == obstacles.CRACK and world.get((x + 1, y - 1)) not in bad_harm_water:
            return actions.RIGHT

    if pls == 'R':
        if world.get((x, y - 1)) == obstacles.CRACK:
            return actions.JUMP
        if world.get((x - 1, y - 2)) == obstacles.CRACK and world.get((x - 1, y - 1)) not in bad_harm_water:
            return actions.LEFT

    if pls == 'L':
        if world.get((x, y - 1)) == obstacles.CRACK:
            return actions.JUMP
        if world.get((x + 1, y - 2)) == obstacles.CRACK and world.get((x + 1, y - 1)) not in bad_harm_water:
            return actions.RIGHT

    # water chek:
    if pls == 'M':
        if world.get((x, y - 1)) == obstacles.WATER:
            return actions.BRAKE
        if world.get((x - 1, y - 2)) == obstacles.WATER and world.get((x - 1, y - 1)) not in bad_harm_crack:
            return actions.LEFT
        if world.get((x + 1, y - 2)) == obstacles.WATER and world.get((x + 1, y - 1)) not in bad_harm_crack:
            return actions.RIGHT

    if pls == 'R':
        if world.get((x, y - 1)) == obstacles.WATER:
            return actions.BRAKE
        if world.get((x - 1, y - 2)) == obstacles.WATER and world.get((x - 1, y - 1)) not in bad_harm_crack:
            return actions.LEFT

    if pls == 'L':
        if world.get((x, y - 1)) == obstacles.WATER:
            return actions.BRAKE
        if world.get((x + 1, y - 2)) == obstacles.WATER and world.get((x + 1, y - 1)) not in bad_harm_crack:
            return actions.RIGHT

    # harm chek:
    if pls == 'M':
        if world.get((x, y - 1)) in harm:
            if world.get((x - 1, y - 1)) not in harm:
                return actions.LEFT
            if world.get((x + 1, y - 1)) not in harm:
                return actions.RIGHT
        return actions.NONE

    if pls == 'R':
        if world.get((x, y - 1)) in harm:
            return actions.LEFT


    if pls == 'L':
        if world.get((x, y - 1)) in harm:
            return actions.RIGHT


    # defult:
    if pls == 'M':
        return actions.NONE
    if pls == 'R' and world.get((x-1, y-1)) not in harm:
        return actions.LEFT
    if pls == 'L' and world.get((x+1, y-1)) not in harm:
        return actions.RIGHT