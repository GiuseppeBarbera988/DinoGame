# Esercizio Python
# Developed by Giuseppe Barbera

def main():
    with open('mazzo.txt', 'r') as f:
        deck = f.readlines()  # reading from file,deck is a list.
    player1 = []  # initializing two lists
    player2 = []
    i = 0  # iterating over the deck
    print(len(deck))
    for k in range(15):  # Just 15 couples of 2 cards
        player1.append(deck[i])
        i += 1
        player2.append(deck[i])
        i += 1
    print("Player 1 hand: {}".format(player1))
    # print(len(player1))
    # print(len(player2))        debug purpose
    print("Player 2 hand: {}".format(player2))
    print('*' * 50)

    # reversing list in order to pop it.
    # Pop picks from the last one, so i reverse it in order to pick the first one
    player1.reverse()
    player2.reverse()
    q = 0  # iterating over while loop
    pt1 = 0  # score first player
    pt2 = 0  # score second player
    carte_tav = 0  # score on the table

    while q < 15:
        card1 = player1.pop()
        print(card1)
        card2 = player2.pop()
        print(card2)
        val1 = decode_card(card1)  # using my function to pick the relative value of the card
        val2 = decode_card(card2)

        if val2 == val1:
            carte_tav += val1 + val2
            print("table: {}".format(carte_tav))
            print('-' * 50)

        elif val1 > val2:
            print("round won by player1")
            pt1 += val1 + val2 + carte_tav
            carte_tav = 0  # resetting table
            print("mom score player1 {}".format(pt1))
            print("mom score player2 {}".format(pt2))
            print('-' * 50)
        elif val2 > val1:
            print("round won by player2")
            pt2 += val1 + val2 + carte_tav
            carte_tav = 0  # resetting variable, clearing table
            print("mom score player1 {} ".format(pt1))
            print("mom score player2 {} ".format(pt2))
            print('-' * 50)
        q += 1
    if pt1 > pt2:
        print("Game won by  player1. Score {}".format(pt1))
    else:
        print("Game won by  player2. Score {}".format(pt2))


def decode_card(card):
    if card == "Verde\n":
        return 3
    elif card == "Rosso\n":
        return 5
    elif card == 'Giallo\n':
        return 1


if __name__ == '__main__':
    main()