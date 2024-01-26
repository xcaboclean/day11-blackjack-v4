from art import logo
import random

class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
    
  def print_card(self):
    if self.rank == '10':
      print("\n")
      print("┌───┐")
      print(f"│{self.rank} │")
      print(f"│ {self.suit} │")
    else:
      print(f"│ {self.rank} │")
      print(f"│ {self.suit} │")
      print("└───┘")


class Hand:
  def __init__(self):
    self.cards=[]

  def add_card(self,card):
    self.cards.append(card)

  def print_hand(self):
    for card in self.cards:
      card.print_card()
      
    
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
    self.player_hand.print_hand()
    
  def play(self):
    print(logo)
    Deck.display_size_deck(self.deck)
    self.initial_cards()
    
    
if __name__ == "__main__":
  game = BlackJackGame()
  game.play()