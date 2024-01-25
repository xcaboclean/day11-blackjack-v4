from art import logo

class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

class BlackJackGame:
  def play(self):
    print(logo)
    
if __name__ == "__main__":
  game = BlackJackGame()
  game.play()