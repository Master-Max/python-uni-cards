import random

class Card:
    def __init__(self, color, suit, value, name, unicode):
        self.color = color
        self.suit = suit
        self.value = value
        self.name = name
        self.unicode = unicode

cardValueNameDict = {
        1: {"name": 'ace', "unicode_ending": int("1", base=16)},
        2: {"name": 'two', "unicode_ending": int("2", base=16)},
        3: {"name": 'three', "unicode_ending": int("3", base=16)},
        4: {"name": 'four', "unicode_ending": int("4", base=16)},
        5: {"name": 'five', "unicode_ending": int("5", base=16)},
        6: {"name": 'six', "unicode_ending": int("6", base=16)},
        7: {"name": 'seven', "unicode_ending": int("7", base=16)},
        8: {"name": 'eight', "unicode_ending": int("8", base=16)},
        9: {"name": 'nine', "unicode_ending": int("9", base=16)},
        10: {"name": 'ten', "unicode_ending": int("a", base=16)},
        11: {"name": 'jack', "unicode_ending": int("b", base=16)},
        12: {"name": 'queen', "unicode_ending": int("d", base=16)},
        13: {"name": 'king', "unicode_ending": int("e", base=16)},
    }

class StandardDeck:
    def __init__(self, size, cards):
        self.size = 52
        self.cards = []
        self.back = chr(int("1f0a0", base=16))

        for x in range(52):
            color = ''
            suit = ''
            value = ''
            name = ''
            unicode = ''

            if x < 13:
                color = 'black'
                suit = 'spades'
                value = x+1
                name = cardValueNameDict[value]["name"]
                tmp_code = cardValueNameDict[value]["unicode_ending"]
                tmp_int = int("1f0a0", base=16) + tmp_code
                unicode = chr(tmp_int)
                mycard = Card(color, suit, value, name, unicode)
                self.cards.append(mycard)
            elif x < 26 :
                color = 'red'
                suit = 'hearts'
                value = (x+1) - 13
                name = cardValueNameDict[value]["name"]
                tmp_code = cardValueNameDict[value]["unicode_ending"]
                tmp_int = int("1f0b0", base=16) + tmp_code
                unicode = chr(tmp_int)
                mycard = Card(color, suit, value, name, unicode)
                self.cards.append(mycard)
            elif x < 39 :
                color = 'red'
                suit = 'diamonds'
                value = (x+1) - 26
                name = cardValueNameDict[value]["name"]
                tmp_code = cardValueNameDict[value]["unicode_ending"]
                tmp_int = int("1f0c0", base=16) + tmp_code
                unicode = chr(tmp_int)
                mycard = Card(color, suit, value, name, unicode)
                self.cards.append(mycard)
            elif x < 52 :
                color = 'black'
                suit = 'clubs'
                value = (x+1) - 39
                name = cardValueNameDict[value]["name"]
                tmp_code = cardValueNameDict[value]["unicode_ending"]
                tmp_int = int("1f0d0", base=16) + tmp_code
                unicode = chr(tmp_int)
                mycard = Card(color, suit, value, name, unicode)
                self.cards.append(mycard)

    def shuffle(self):
        random.shuffle(self.cards)

    def flash(self):
        for x in range(len(self.cards)):
            print('===============')
            print("num {} of {}".format(x+1, len(self.cards)))
            print("{} {}".format(self.cards[x].unicode, self.back))
            # print(mydeck.back)
            print("{} of {}".format(self.cards[x].name, self.cards[x].suit))
            print("{} | {}".format(self.cards[x].color, self.cards[x].value))
            print('--------------')


mydeck = StandardDeck(52, [])


for x in range(52):
    print('===============')
    print("{} {}".format(mydeck.cards[x].unicode, mydeck.back))
    # print(mydeck.back)
    print(mydeck.cards[x].color)
    print(mydeck.cards[x].value)
    print(mydeck.cards[x].name)
    print(mydeck.cards[x].suit)
    print('--------------')


print(len(mydeck.cards))

acard = mydeck.cards.pop(2)

print(acard.name + " of " + acard.suit)

print(len(mydeck.cards))

mydeck.shuffle()

for x in range(len(mydeck.cards)):
    print('===============')
    print("{} {}".format(mydeck.cards[x].unicode, mydeck.back))
    # print(mydeck.back)
    print(mydeck.cards[x].color)
    print(mydeck.cards[x].value)
    print(mydeck.cards[x].name)
    print(mydeck.cards[x].suit)
    print('--------------')


mydeck.flash()


mydeck.cards.append(acard)

mydeck.flash()


dealer_hand = []

player_hand = []

mydeck.shuffle()

dealer_hand.append(mydeck.cards.pop(0))
player_hand.append(mydeck.cards.pop(0))
dealer_hand.append(mydeck.cards.pop(0))
player_hand.append(mydeck.cards.pop(0))

dealer_total = 0
for x in range(len(dealer_hand)):
    print("{} of {}".format(dealer_hand[x].name, dealer_hand[x].suit))
    if dealer_hand[x].value == 1:
        dealer_total += 11
    elif dealer_hand[x].value >= 10:
        dealer_total += 10
    else:
        dealer_total += dealer_hand[x].value

print("Dealer Total: {}".format(dealer_total))
print("+++++++++++++++++")

player_total = 0
for x in range(len(player_hand)):
    print("{} of {}".format(player_hand[x].name, player_hand[x].suit))
    if player_hand[x].value == 1:
        player_total += 11
    elif player_hand[x].value >= 10:
        player_total += 10
    else:
        player_total += player_hand[x].value

print("player Total: {}".format(player_total))
