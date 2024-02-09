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
    
  def display_size_deck(self):
    print(f"\n┌───────────────┐\n│{len(self.cards):03}🃏🎴 card(s)│\n└───────────────┘")
  
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
  
  def play(self):
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
      clear()
      print(logo)
      Deck.display_size_deck(self.deck)
      self.initial_cards()    
    
if __name__ == "__main__":
  game = BlackJackGame()
  game.play()