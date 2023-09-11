"Deck of Card compilation"
import collections
Card = collections.namedtuple('card',['rank','suits'])
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
        # [['2','spades'],['3','spades'],['4','spades']....]
    def __len__(self):
        return(len(self._cards))
       #return 10

    def __getitem__(self,position):
        return self._cards[position]

"Sorted cards (2,3,4,5,6,7,8,9,10,J,Q,K,A) for suits in order (Clubs, Diamond, Heart then Spade )"
deck = FrenchDeck()
print(FrenchDeck.ranks)
suit_values = dict(clubs = 39, diamonds = 26, hearts = 13, spades = 0)
def club_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return(rank_value + suit_values[card.suits])
for card in sorted(deck,key=club_high):
    print(card)

# print(len(deck))
# print(deck[0])
# deck[13]
# from random import choice
# print(choice(deck))
# print(choice(deck))
# print(choice(deck))
# print(deck[:3])
# print(deck[-13:])
# for card in deck:
#     print(card)
# # for card in reversed(deck):
# #     print(card)
# for card in reversed(deck[12::13]):
#     print(card)
# if card in deck:
#    # print(card)
#     print(Card("7","hearts") in deck)
# # for card in sorted(deck):
# #     print(card)


