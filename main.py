from replit import clear
from art import logo
import random


class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

  def __str__(self):
    return f"{self.rank} of {self.suit}"
    
  def card_drawing(self):
    
    if self.rank == '10':
      drawn_card = ["\n","┌───┐", f"│{self.rank} │", f"│ {self.suit} │", "└───┘"]
    else:
      drawn_card = ["\n", "┌───┐", f"│ {self.rank} │", f"│ {self.suit} │", "└───┘"]
    return " ".join(drawn_card)


class Hand:
  def __init__(self):
    self.cards=[]

  def add_card(self,card):
    self.cards.append(card)

  def print_hand(self):
    print("Your hand:")
    hand_drawing = ""
    for card in self.cards:
      hand_drawing.join(card.card_drawing())

    print(hand_drawing)
    
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
      
#***********************************************************
  
  def display_hands_with_card_drawing(self, reveal_dealer = False):
      self.player_hand.print_hand()
      print("Dealer's hand:")
      if reveal_dealer:
        self.dealer_hand.print_hand()
        
  #***********************************************************
  
  def play(self):
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
      while True:
        clear()
        print(logo)
        Deck.display_size_deck(self.deck)
        self.initial_cards()
        self.display_hands_with_card_drawing(reveal_dealer=False)
        resposta = input("Be continue? (y/n): ")
        if resposta.lower() != 'y':
            break
    
if __name__ == "__main__":
  game = BlackJackGame()
  game.play()