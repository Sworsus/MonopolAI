class Card:
    '''
    effects:
        0 : pay
        1 : payProperties
        2 : payToPlayers
        3 : earn
        4 : earnFromPlayers
        5 : moveBy
        6 : moveTo
        7 : moveToNextStation
        8 : prison
        9 : freePrison
        10: moveToNextCompany
    '''

    def __init__(self, id, data, type):
        self.id = id
        self.data = data
        self.type = type
