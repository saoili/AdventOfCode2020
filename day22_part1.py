FILENAME = 'day22_part1_eg1.txt'
FILENAME = 'day22_part1.txt'

# FILENAME = 'day22_part1_eg2.txt'
# FILENAME = 'day22_part2.txt'
# FILENAME = 'day22_part2_eg1.txt'
# FILENAME = 'day22_part2_eg2.txt'


def get_starting_decks():
  players = {}
  player_number = None

  with open(FILENAME, 'r') as file:
    players = file.read().split("\n\n")
    player1, player2 = [[int(c) for c in p.split("\n")[1:]] for p in players]

  return player1, player2


class Game():
  def __init__(self, player1_deck, player2_deck):
    self.players = {1: player1_deck, 2: player2_deck}
    self.round = 0

  def play_round(self):
    """Returns True at game end, False otherwise"""
    self.round += 1
    player1_card = self.players[1].pop(0)
    player2_card = self.players[2].pop(0)

    if player1_card > player2_card:
      print(f"player 1 wins round {self.round}")
      self.players[1] += [player1_card, player2_card]
    else:  # player 2 card is higher, no two copies of a card
      print(f"player 2 wins round {self.round}")
      self.players[2] += [player2_card, player1_card]

    if self.players[1] == []:
      self.winner = 2
      print(f"and the game!")
      return True
    elif self.players[2] == []:
      self.winner = 1
      print(f"and the game!")
      return True

    return False

  def play_out(self):
    finished = False

    while not finished:
      finished = self.play_round()

    print(f"and the winner is {self.winner}", end=" ")
    print(f"with deck {self.players.get(self.winner)}")

    self.winning_score = 0

    for i, card in enumerate(self.players.get(self.winner)[::-1]):
      self.winning_score += (i + 1) * card

    print(f"with a winning score of {self.winning_score}")


# class Deck():
#   def __init__(self, deck_size):
#     self.cards = [i for i in range(deck_size)]
#     self.shuffles = {
#       'deal_into_new_stack': self.deal_into_new_stack,
#       'cut_n_cards': self.cut_n_cards,
#       'deal_with_increment_n': self.deal_with_increment_n,
#     }

#   def deal_into_new_stack(self):
#     self.cards = self.cards[::-1]

#   def cut_n_cards(self, n):
#     self.cards = self.cards[n:] + self.cards[:n]

#   def deal_with_increment_n(self, n):
#     old_cards = self.cards.copy()
#     j = 0
#     l = len(self.cards)

#     for card in old_cards:
#       self.cards[j] = card
#       j = (j + n) % l


def main():
  # deck = Deck(DECK_SIZE)
  # print(deck.cards)
  # # deck.deal_into_new_stack()
  # # print(deck.cards)
  # # deck.cut_n_cards(-4)
  # deck.deal_with_increment_n(3)
  # print(deck.cards)
  starting_decks = get_starting_decks()
  game = Game(*starting_decks)

  print(game)
  print(game.play_out())

if __name__ == '__main__':
  main()
