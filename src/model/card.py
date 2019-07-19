class Card:
    '''
    effects:
        0 : pay
        1 : payProperties
        2 : earn
        3 : earnFromPlayers
        4 : moveBy
        5 : moveTo
        6 : prison
    '''

    def __init__(self, id, data, type):
        self.id = id
        self.data = data
        self.type = type
