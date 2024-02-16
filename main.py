from replit import clear
from art import logo
import random


class Card:
  
  def __init__(self, rank, suit):
    
    self.rank = rank
    self.suit = suit

  
  def __str__(self):
    
    return f"{self.rank} of {self.suit}"
    

class Hand:

  def __init__(self):
    self.cards=[]

  def add_card(self,card):
    self.cards.append(card)

  def get_value(self):
    value = 0
    num_aces = 0
    for card in self.cards:
      if card.rank == 'A':
        num_aces +=1
        value += 11
      elif card.rank in ['K','Q','J']:
        value += 10
      else:
        value += int(card.rank)
  
    while value > 21 and num_aces:
      value -= 10
      num_aces -=1
    return  value
    
    
class Deck:
  def __init__(self):
      ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
      suits = ["♠️", "♣️", "♥️", "♦️", "♠️", "♣️", "♥️", "♦️"]
      self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
      random.shuffle(self.cards)
    
  def draw_card(self):
    return self.cards.pop()

class BlackJackGame:
  def __init__(self):
    self.deck = Deck()
    self.player_hand = Hand()
    self.dealer_hand = Hand()

  def initial_cards(self):
    self.player_hand.add_card(self.deck.draw_card())
    self.dealer_hand.add_card(self.deck.draw_card())
    self.player_hand.add_card(self.deck.draw_card())
    self.dealer_hand.add_card(self.deck.draw_card())

    
  def display_hands(self, reveal_dealer=False):
    print("Your hand:", ', '.join(str(card) for card in self.player_hand.cards))
    if reveal_dealer:
        print("Dealer's hand:", ', '.join(str(card) for card in self.dealer_hand.cards))
    else:
        print("Dealer's hand:", str(self.dealer_hand.cards[0]) + ", [Hidden Card]")

  def player_turn(self):
    while True:
      self.display_hands()
      player_value = self.player_hand.get_value()

      if player_value == 21:
        print("Blackjack! You win!")
        return
        
      if player_value > 21 :
        print("Bust! You lose.")
        return
        
      action = input("Do you want to 'hit' or 'stand': ").lower()

      if action == 'hit':
        self.player_hand.add_card(self.deck.draw_card())
      elif action == 'stand':
        break
      else:
        print("Invalid action. Please enter 'hit' or 'stand'.")

  def dealer_turn(self):
    while self.dealer_hand.get_value() < 17:
      self.dealer_hand.add_card(self.deck.draw_card())

  def determine_winner (self):
    player_score = self.player_hand.get_value()
    dealer_score = self.dealer_hand.get_value()
    print(f"You score -> {player_score}")
    print(f"Dealer score -> {dealer_score}")
    
    if player_score > 21:
      return "Player Bust! You lose!"
    elif dealer_score >21:
      return "Dealer Bust! You Win!"
    elif player_score > dealer_score:
      return "You Win!"
    elif dealer_score > player_score:
      return "You Lose!"
    else:
      return "Tie!"
  
  def play(self):
    clear()
    print(logo)

    self.initial_cards()
    self.player_turn()
    self.dealer_turn()
    self.display_hands(reveal_dealer=True)
    result = self.determine_winner()
    print(result)
      
if __name__ == "__main__":
  while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    game = BlackJackGame()
    game.play()