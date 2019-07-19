import itertools
import random
class Tabletop:
    def __init__(self, nPlayers, properties, places):
        self.players = [Player(i) for i in range(nPlayers)]
        self.properties = properties
        self.places = places
        self.nPlaces = len(places)
        possibleOrders = list(itertools.permutations(range(nPlayers)))
        turnOrder = possibleOrders[random.randInt(0, len(possibleOrders)-1)]
