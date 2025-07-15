import random
import time

class Card:
    def __init__(self, color, suit, value, name, unicode):
        self.color = color
        self.suit = suit
        self.value = value
        self.name = name
        self.unicode = unicode

def calculateScore(arr):
    non_ace_cards = []
    ace_cards = []
    for x in range(len(arr)):
        if(arr[x].name == 'ace'):
            ace_cards.append(arr[x])
        else:
            non_ace_cards.append(arr[x])

    total = 0

    for x in range(len(non_ace_cards)):
        if(non_ace_cards[x].value >= 10 ):
            total += 10
        else:
            total += non_ace_cards[x].value

    for x in range(len(ace_cards)):
        if(total + 11 > 21):
            total += 1
        else:
            total += 11
    
    return total
    # look at array
    # if array contains any aces, split array into non ace cards and ace cards
    # add array of non ace cards
    # if total of non ace cards is greater than 21 then bust
    # else continue
    # add ace cards one at a time
    # check total of non ace and current card from ace array
    # if +11 is greater than 21 add 1
    # repeat until no more aces in the ace array
    # if total is greater than 21 then bust
    # actually this funcion shouldn't determine if you bust, it should just return the result

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
mydeck.shuffle()

dealer_hand = []
player_hand = []

dealer_hand.append(mydeck.cards.pop(0))
player_hand.append(mydeck.cards.pop(0))
dealer_hand.append(mydeck.cards.pop(0))
player_hand.append(mydeck.cards.pop(0))

game_running = True
player_turn = True

while(game_running):
    print("====================")
    if(player_turn):
        print("Dealer Total: {} + ?".format(calculateScore([dealer_hand[0]])))
        print("{} of {}".format(dealer_hand[0].name, dealer_hand[0].suit))
        print("? of ?")
        print("--------------------")
        print("Player Total: {}".format(calculateScore(player_hand)))
        for x in range(len(player_hand)):
            print("{} of {}".format(player_hand[x].name, player_hand[x].suit))
        print("====================")
        if(calculateScore(player_hand) <= 21):
            player_action = input('(H)it or (S)tay? ')
            if(player_action[0].lower() == 'h'):
                player_hand.append(mydeck.cards.pop(0))
            elif(player_action[0].lower() == 's'):
                player_turn = False
            else:
                print('Error: Not a valid action')
        else:
            print('BUST!')
            player_turn = False
    else:
        print("Dealer Total: {}".format(calculateScore(dealer_hand)))
        for x in range(len(dealer_hand)):
            print("{} of {}".format(dealer_hand[x].name, dealer_hand[x].suit))
        print("--------------------")
        print("Player Total: {}".format(calculateScore(player_hand)))
        for x in range(len(player_hand)):
            print("{} of {}".format(player_hand[x].name, player_hand[x].suit))
        print("====================")
        
        if(calculateScore(dealer_hand) > 21):
            print("You Win!")
            game_running = False
        elif(calculateScore(player_hand) > 21):
            print("The House Wins")
            game_running = False
        elif(calculateScore(player_hand) < calculateScore(dealer_hand)):
            print("The House Wins")
            game_running = False
        elif(calculateScore(player_hand) == 21 and calculateScore(dealer_hand) == 21):
            print("Tie Game")
            game_running = False
        elif(calculateScore(player_hand) == calculateScore(dealer_hand)):
            print("Tie Game")
            game_running = False
        elif(calculateScore(player_hand) > calculateScore(dealer_hand)):
            print("Dealer Will (H)it")
            time.sleep(2)
            dealer_hand.append(mydeck.cards.pop(0))
        else:
            print("You Win!")
            game_running = False




# dealer_total2 = calculateScore(dealer_hand)
# print("Dealer Total: {}".format(dealer_total2))

# print("+++++++++++++++++")

# player_total2 = calculateScore(player_hand)

# print("player Total: {}".format(player_total2))
