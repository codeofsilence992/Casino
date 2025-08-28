def main():
    import random
    from time import sleep
    def blackjack():
        deck = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "King": 10, "Queen": 10}
        coins = 5




        def print_cards(hidedealercard=True):
            if hidedealercard:
                player_cards_printable = "  ".join(player_cards)
                dealer_cards_printable = "  ".join(dealer_cards)
                width = 30
                print("==========YOUR CARDS==========  ========DEALER'S CARDS========")
                print("")
                print(player_cards_printable.center(width) + "  " + (dealer_cards_printable + "  ?").center(width))
                print("")
                print("=" * width + "  " + "=" * width)
                print(("Total: " + f"{playertotal}").center(width) + "  " + ("Total: " + f"{dealertotal}" +  " + ?").center(width))
            elif not hidedealercard:
                player_cards_printable = "  ".join(player_cards)
                dealer_cards_printable = "  ".join(dealer_cards)
                width = 30
                print("==========YOUR CARDS==========  ========DEALER'S CARDS========")
                print("")
                print(player_cards_printable.center(width) + "  " + dealer_cards_printable.center(width))
                print("")
                print("=" * width + "  " + "=" * width)
                print(("Total: " + f"{playertotal}").center(width) + "  " + ("Total: " + f"{dealertotal}").center(width))



        def stay():
            nonlocal dealertotal
            nonlocal dealer_cards
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
                    aces += 1
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
                    aces += 1
                else:
                    total += deck.get(card, 0)
            while total > 21 and aces > 0:
                total -= 10
                aces -= 1
            return total


        def hit():
            nonlocal player_cards
            nonlocal playertotal
            player_cards.append(random.choice(list(deck.keys())))
            playertotal = calculate_player_total()
            print_cards()

        blackjack_running = True
        print("=" * 26)
        print("")
        print("WELCOME TO MAC'S BLACKJACK".center(26))
        print("")
        print("=" * 26)

        while blackjack_running:
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
                print_cards()

                while in_round:
                    if playertotal == 21:
                        print("Player hit a blackjack!")
                        print(f"You won {round(bet / 2)} coins!")
                        coins += round(bet / 2)
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
                        print_cards(hidedealercard=False)
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

            print("You have no more money!")
            while True:
                print("Play again [P]")
                print("Quit [Q]")
                choice1 = input("> ").lower().strip()
                if choice1 == "p":
                    coins = 5
                    break
                elif choice1 == "q":
                    print("Thank you for playing!")
                    blackjack_running = False
                    break
                else:
                    continue




    def slots():
        def spin():
            result = []
            for x in range(0, 3):
                result.append(str(random.randint(1, 5)))
            print("*" * 15)
            print((" | ".join(result)).center(15))
            print("*" * 15)
            if result.count(result[0]) == 3:
                return 1
            else:
                return 0

        print("=" * 22)
        print("")
        print("WELCOME TO MAC'S SLOTS".center(22))
        print("")
        print("=" * 22)

        is_running = True
        amount = 100

        while is_running:
            if amount <= 0:
                print("You have no more money!")
            while amount <= 0:
                print("Play again [P]")
                print("Quit [Q]")
                option = input("> ").strip().lower()
                if option == "p":
                    amount = 100
                elif option == "q":
                    print("Thank you for playing!")
                    is_running = False
                    break
                else:
                    continue
            if amount <= 0:
                break
            print(f"Balance: ${amount}")
            bet = 0
            print("Place your bet: ")
            while True:
                try:
                    bet = int(input("> "))
                    if bet <= 0:
                        continue
                    elif bet > amount:
                        print("You don't have enough!")
                    else:
                        break
                except ValueError:
                    continue
            go = spin()
            if go == 1:
                amount += bet * 10
            else:
                amount -= bet

    try:
        game_is_running = True
        while game_is_running:
            print("Welcome to Mac's Casino! ")
            print("Blackjack [B]")
            print("Slots [S]")
            print("Quit [Q]")
            while True:
                option = input("> ").strip().lower()
                if option == "b":
                    blackjack()
                    break
                elif option == "s":
                    slots()
                    break
                elif  option == "q":
                    game_is_running = False
                    break
                else:
                    print("Please pick a valid option!")
    except KeyboardInterrupt:
        print("I hope you enjoyed my game! ")
        sleep(0.5)

if __name__ == "__main__":
    main()