class Game:
    def __init__(self, nPlayers):
        #TODO: load properties and places
        properties = None
        places = None
        self.table = Tabletop(nPlayers, properties, places)
