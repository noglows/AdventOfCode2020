from pprint import pprint

# Open and read data
cards = open("/Users/jess/Documents/Code/Advent2020/22/Data.txt", "r")
cards = cards.readlines()

player_1_deck = []
player_2_deck = []
player = "1"
title_row = False

# comparison function
def compare_cards(p1, p2):
    p1 = int(p1)
    p2 = int(p2)
    if p1 >= p2: 
        return True
    else: 
        return False


def calc_score(deck):
    total = 0
    high = len(deck)
    for item in deck:
        item = int(item)
        total += item * high
        high = high - 1
    return total


# Create the decks as arrays
for card in cards:
    title_row = False
    card = card.replace("\n", "")
    if card == "Player 1:":
        player = "1"
        title_row = True
    elif card == "Player 2:":
        title_row = True
        player = "2"


    if card == "":
        print("blank")
    elif player == "1" and title_row == False:
        player_1_deck.append(card)
    elif player == "2" and title_row == False:
        player_2_deck.append(card)



still_going = True
i = 0

while still_going == True:

    compare = compare_cards(player_1_deck[0], player_2_deck[0])
    if compare == True:
        p2_pull = player_2_deck.pop(0) 
        p1_pull = player_1_deck.pop(0) 
        player_1_deck.append(p1_pull)
        player_1_deck.append(p2_pull)
    else: 
        p2_pull = player_2_deck.pop(0) 
        p1_pull = player_1_deck.pop(0) 
        player_2_deck.append(p2_pull)
        player_2_deck.append(p1_pull)

    if len(player_1_deck) == 0 or len(player_2_deck) == 0:
        still_going = False

    i +=1 

print("Part One Solution is: ")
deck_1_score = calc_score(player_1_deck)
deck_2_score = calc_score(player_2_deck)

if deck_1_score > deck_2_score:
    print (deck_1_score)
else: print(deck_2_score)



