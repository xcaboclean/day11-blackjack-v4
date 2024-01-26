from art import logo
import random

class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

class Hand:
  def __init__(self):
    self.cards=[]
    
class Deck:
  def __init__(self):
      ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
      suits = ["♠️", "♣️", "♥️", "♦️", "♠️", "♣️", "♥️", "♦️"]
      self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
      random.shuffle(self.cards)
    
  def display_size_deck(self):
    print(f"\n┌───────────────┐\n│{len(self.cards):03}🃏🎴 card(s)│\n└───────────────┘")

class BlackJackGame:
  def __init__(self):
    self.deck = Deck()

  def play(self):
    print(logo)
    Deck.display_size_deck(self.deck)
    
if __name__ == "__main__":
  game = BlackJackGame()
  game.play()