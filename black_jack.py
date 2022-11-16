
import random


class Deck():
    def __init__(self):
        self.deck = []
        self.suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        self.cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

        for i in range(0, len(self.suits)):
            for n in range(0, len(self.cards)):
                self.deck.append([self.suits[i],self.cards[n]])
        # print(self.deck)


#     def cardCount(self):
#         print(len(self.deck))

class Game:
    def __init__(self, deck):
        self.player_cards = []
        self.dealer_cards = []
        self.player_score = 0
        self.dealer_score = 0
        self.deck = deck.deck
        
    def showPlayer(self):
        print(text['hit_or_stand'])
    
    def showDealer(self):
        print(text['hit_or_stand'])
        
    def dealHandPlayer(self):
        # print(self.deck)
        while len(self.player_cards) < 2:
            player_card = random.choice(self.deck)
            self.player_cards.append(player_card)
            self.deck.remove(player_card)
        self.player_score = int(self.player_cards[0][1]) + int(self.player_cards[1][1])
            
    def dealHandDealer(self):
        while len(self.dealer_cards) < 2:
            dealer_card = random.choice(self.deck)
            self.dealer_cards.append(dealer_card)
            self.deck.remove(dealer_card)
        self.dealer_score = int(self.dealer_cards[0][1]) + int(self.dealer_cards[1][1])
        
        print(f'The dealers up card is: {self.dealer_cards[0]}')
#         print(self.player_score)
#         print(self.dealer_score)

    def hitMePlayer(self):
        if self.player_score < 21:
            player_new_card = random.choice(self.deck)
            self.player_cards.append(player_new_card)
            self.deck.remove(player_new_card)
            self.player_score += int(player_new_card[1])
#             print(self.player_cards)
#             print(self.player_score)
            
    def hitMeDealer(self):
        if self.dealer_score < 21:
            dealer_new_card = random.choice(self.deck)
            self.dealer_cards.append(dealer_new_card)
            self.deck.remove(dealer_new_card)
            self.dealer_score += int(dealer_new_card[1])
#             print(self.dealer_cards)
#             print(self.dealer_score)
            
              

def main():

    while True:
        start_game = input(text['welcome'])
        if start_game == 'yes' or start_game == 'Yes':
            new_deck = Deck()
            new_game = Game(new_deck)
            new_game.dealHandPlayer()
            new_game.dealHandDealer()
            print(text['deal'], new_game.player_cards)
            hitStand = input(f'Your current card count is {new_game.player_score}. Would you like to Hit or Stand?: ')
        if hitStand == 'hit' or hitStand == 'Hit':
            while new_game.player_score <= 21:
                new_game.hitMePlayer()
                if new_game.player_score > 21:
                    print(f' Your new hand is: {new_game.player_cards}')
                    lose = input(f'You busted!.. Your score is {new_game.player_score}. Do you want to try again?: ')
                else:
                    print(f' Your new hand is: {new_game.player_cards}')
                    still_in = input(f'Your current card count is {new_game.player_score}. Would you like to Hit or Stand?: ')
        if hitStand == 'stand' or hitStand == 'Stand':
            still_in = ''
            print('Dealer is playing..')
            while new_game.dealer_score <= 21:
                new_game.hitMeDealer()
                if new_game.dealer_score > 21:
                    print(f' Your new hand is: {new_game.dealer_cards}')
                    lose = input(f'The dealers hand is {new_game.dealer_score}. The dealer busted.. Your Win! Play Again? ')
                else:
                    print(f' Dealers hand is: {new_game.dealer_cards}')
                    still_in = input(f'Dealers card count is {new_game.dealer_score}. Should the dealer Hit or Stand?: ')
                                
            if still_in == 'stand' or still_in == 'Stand':
                
        
            

main()
