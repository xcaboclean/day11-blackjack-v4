from replit import clear
from art import logo
import random


class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

  def __str__(self):
    return f"{self.rank} of {self.suit}"

  
  ''' def drawing(self, lines, reveal_dealer):

    lines[0] += "┌───┐"
    
    if self.rank == '10':      
      lines[1] += f"│{self.rank} │"
    else:
     lines[1] += f"│ {self.rank} │"
    
    lines[2] += f"│ {self.suit} │"
    lines[3] += "└───┘"

    if reveal_dealer:
      lines[1] = " │ ? │"
      lines[2] = " │ ? │"
      
    return lines
'''
      

class Hand:

  def __init__(self):
    self.cards=[]

  def add_card(self,card):
    self.cards.append(card)

  def assemble_hand(self, reveal_dealer):
    lines = ["","","",""]
    
    print("Your hand:")
    for card in self.cards:
      lines += card.drawing(lines,reveal_dealer)
    return lines
    
  def print_hand(lines, reveal_dealer):
    
    
    
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

#***********************************************************

  def display_hands(self, reveal_dealer=False):
    print("Your hand:", ', '.join(str(card) for card in self.player_hand.cards))
    if reveal_dealer:
        print("Dealer's hand:", ', '.join(str(card) for card in self.dealer_hand.cards))
    else:
        print("Dealer's hand:", str(self.dealer_hand.cards[0]) + ", [Hidden Card]")
      

  
'''def display_hands_with_card_drawing(self, reveal_dealer):
  
  self.player_hand.print_hand(False)
  print("Dealer's hand:") 
  self.dealer_hand.print_hand(True)'''
  
def play(self):
  while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    print(logo)
    Deck.display_size_deck(self.deck)
    self.initial_cards()
    
    #self.display_hands_with_card_drawing(reveal_dealer=False)
    #resposta = input("Be continue? (y/n): ")
    #if resposta.lower() != 'y':
    #  break
    
if __name__ == "__main__":
  game = BlackJackGame()
  game.play()