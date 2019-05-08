class Card():
    RANKS=[]
    SUITS=[]

    def __init__(self, rank, suit, face_up=True):
        self.rank=rank
        self.suit=suit
        self.is_face_up=face_up #face for true and vice versa
        return super().__init__(*args, **kwargs)
    def __str__(self):
        return super().__str__()
    def flip(self):
        self.is_face_up=not self.is_face_up

class Hand():
    def __init__(self, *args, **kwargs):
        self.cards=[]
        return super().__init__(*args, **kwargs)
    def __str__(self):
        if self.
        return super().__str__()
class Poke():
    #
    def populate(self):
    def deal():
if __name__ == "__main__":
    players=[Hand(),Hand(),Hand(),Hand()]
    poke1=Poke()
    poke1.populate()
    poke1.suffle()
    poke1.deal(players)
