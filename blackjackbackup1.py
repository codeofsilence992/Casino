import random
from time import sleep
deck = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "King": 10, "Queen": 10}
coins = 5
bet = 0



def print_cards():
    print("Your cards:")
    for x in player_cards:
        print(x)
    print(f"Your total: {playertotal}")

def stay():
    global dealertotal
    global dealer_cards
    dealer_cards.append(random.choice(list(deck.keys())))
    dealertotal = calculate_dealer_total()
    while dealertotal < 17:
        dealer_cards.append(random.choice(list(deck.keys())))
        dealertotal = calculate_dealer_total()


def calculate_player_total():
    total = 0
    aces = 0
    for card in player_cards:
        if card == "Ace":
            total += 11
        else:
            total += deck.get(card, 0)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def calculate_dealer_total():
    total = 0
    aces = 0
    for card in dealer_cards:
        if card == "Ace":
            total += 11
        else:
            total += deck.get(card, 0)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


def hit():
    global player_cards
    global playertotal
    player_cards.append(random.choice(list(deck.keys())))
    playertotal = calculate_player_total()
    print_cards()



while coins > 0:
    while True:
        print(f"Coins: {coins}")
        in_round = True
        try:
            bet = int(input("How many coins will you bet?"))
            if bet > coins:
                print("You don't have enough.")
            else:
                break
        except ValueError:
            print("You need to enter a valid number!")
    playertotal = 0
    dealertotal = 0
    player_cards = []
    dealer_cards = []
    for x in range(0, 2):
        player_cards.append(random.choice(list(deck.keys())))
        playertotal = calculate_player_total()
    dealer_cards.append(random.choice(list(deck.keys())))
    dealertotal = calculate_dealer_total()
    print("Dealer cards:")
    print("".join(dealer_cards))
    print("?")
    print("Your cards:")
    for x in player_cards:
        print(x)
    print(f"Your total: {playertotal}")

    while in_round:
        if playertotal == 21:
            print("Player hit a blackjack!")
            print(f"You won {bet / 2} coins!")
            coins += bet / 2
            break
        elif playertotal > 21:
            print("Player busted!")
            print(f"You lost {bet} coins!")
            coins -= bet
            break
        hitorstay = input("Hit [H] or stay [S]?").lower()
        if hitorstay == "h":
            hit()
        elif hitorstay == "s":
            stay()
            print("Dealer cards:")
            for x in dealer_cards:
                print(x)
            print(f"Dealer total: {dealertotal}")
            for x in player_cards:
                print(x)
            print(f"Your total: {playertotal}")
            if dealertotal > 21:
                print("Dealer busted!")
                print(f"You won {bet} coins!")
                coins += bet
                break
            else:
                if dealertotal > playertotal:
                    print("Dealer's total was more than player's total!")
                    print(f"You lost {bet} coins!")
                    coins -= bet
                    break
                elif playertotal > dealertotal:
                    print("Player's total was more than dealer's total!")
                    print(f"You won {bet} coins!")
                    coins += bet
                    break
                elif playertotal == dealertotal:
                    print("The player and dealer's totals were both the same!")
                    print("You didn't lose or win any coins.")
                    break
        else:
            print("Pick a valid option!")

print("You have no more coins to bet.")