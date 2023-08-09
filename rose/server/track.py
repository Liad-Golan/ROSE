import random
from rose.common import config, obstacles


class Track(object):

    def __init__(self):
        self._matrix = None
        self.reset()

    # Game state interface

    def update(self):
        """ Go to the next game state """
        self._matrix.pop()
        self._matrix.insert(0, self._generate_row())

    def state(self):
        """ Return read only serialize-able state for sending to client """
        items = []
        for y, row in enumerate(self._matrix):
            for x, obs in enumerate(row):
                if obs != obstacles.NONE:
                    items.append({"name": obs, "x": x, "y": y})
        return items

    # Track interface

    def get(self, x, y):
        """ Return the obstacle in position x, y """
        return self._matrix[y][x]

    def set(self, x, y, obstacle):
        """ Set obstacle in position x, y """
        self._matrix[y][x] = obstacle

    def clear(self, x, y):
        """ Clear obstacle in position x, y """
        self._matrix[y][x] = obstacles.NONE

    def reset(self):
        self._matrix = [[obstacles.NONE] * config.matrix_width
                        for x in range(config.matrix_height)]

    # Private

    def _generate_row(self):
        """
        Generates new row with obstacles

        Try to create fair but random obstacle stream. Each player get the same
        obstacles, but in different cells if 'is_track_random' is True.
        Otherwise, the tracks will be identical.
        """
        row = [obstacles.NONE] * config.matrix_width
        obstacle = obstacles.get_random_obstacle() #choses a random obsticle
        if config.is_track_random:
            for player in range(config.max_players): #does these actions for every player.
                low = player * config.cells_per_player #low is the closest lane to the left of a player.
                high = low + config.cells_per_player #high is the closest lane to the left of the player + 1.
                cell = random.choice(range(low, high)) # picks a random cell/lane from the players lane
                row[cell] = obstacle #changes the picked cell to be the previously chosen obstacle
        else:
            cell = random.choice(range(0, config.cells_per_player))
            for lane in range(config.max_players):
                row[cell + lane * config.cells_per_player] = obstacle
        return row
