INPUT_EG1 = "389125467"
INPUT = "962713854"


class Cup():
  def __init__(self, value):
    self.value = value
    self.to_the_right = None
    self.to_the_left = None

  def __str__(self):
    return str(self.value)


class CupGame():
  def __init__(self, cups_string, max_num=None):
    self.cups = set()
    self.current_cup = None
    self.size = len(cups_string)
    self.turn = 0
    self.cups_dict = {}
  
    cups_int = [int(i) for i in cups_string]
    max_cups_int = max(cups_int)

    self.min_in_circle = min(cups_int)
    if max_num is None:
      self.max_in_cirle = max(cups_int)
    else:
      self.max_in_cirle = max_num

    if max_num is not None:
      while max_cups_int < max_num:
        max_cups_int += 1
        cups_int.append(max_cups_int)

    for i in cups_int:
      # print(f"i is {i}")
      c = Cup(i)

      if i == 1:
        self.one_cup = c
      if self.current_cup is None:
        # print(f"making it self.current_cup")
        self.current_cup = c
        self.start_print_at = c
      else:
        # print(f"we already ahd a current_cup")
        c.to_the_left = last_cup
        # print(f"setting {last_cup.value} as to the left of {c.value}")
        last_cup.to_the_right = c
        # print(f"setting {c.value} as to the right of {last_cup.value}")
      last_cup = c
      self.cups.add(c)
      self.cups_dict[i] = c

    # print(f"last c is {c}")
    # print(f"setting {self.current_cup.value} as to the right of {c.value}")
    # print(f"and {c.value} as to the right of {self.current_cup}")
    c.to_the_right = self.current_cup
    self.current_cup.to_the_left = c

    # print(f"self.cups is {[str(c) for c in self.cups]}")
    # print(f"with len {len(self.cups)}")

  def part_two_ans(self):
    right = self.one_cup.to_the_right
    two_right = right.to_the_right
    return right.value * two_right.value

  def __str__(self):
    ret_val = ""
    next_cup = self.one_cup.to_the_right
    # print(f"next_cup is {next_cup}")

    for i in range(self.size-1):
      # print(f"the next cup is {next_cup.to_the_right}")
      ret_val = ret_val + str(next_cup.value)
      next_cup = next_cup.to_the_right

    return ret_val

  def take_turn(self):
    self.turn += 1

    first = self.current_cup.to_the_right
    second = first.to_the_right
    third = second.to_the_right
    forth = third.to_the_right

    self.current_cup.to_the_right = forth
    forth.to_the_left = self.current_cup

    destination_value = self.current_cup.value
    destination = None

    max_in_cirle = self.max_in_cirle
    while self.cups_dict[max_in_cirle] in (first, second, third):
      max_in_cirle -= 1

    min_in_circle = self.min_in_circle
    while self.cups_dict[min_in_circle] in (first, second, third):
      min_in_circle += 1

    while destination is None:
      destination_value -= 1

      if destination_value < min_in_circle:
        destination_value = max_in_cirle

      possible_destination = self.cups_dict.get(destination_value)

      if possible_destination not in (first, second, third):
        destination = possible_destination

    to_the_right = destination.to_the_right

    third.to_the_right = to_the_right
    to_the_right.to_the_left = third

    first.to_the_left = destination
    destination.to_the_right = first

    self.current_cup = self.current_cup.to_the_right


def main():
  # cup_game = CupGame(INPUT_EG1, 1000000)
  cup_game = CupGame(INPUT, 1000000)
  print("here")
  print(cup_game)
  for i in range(10000000):
    cup_game.take_turn()
    turn = cup_game.turn
    if turn % 100000 == 0:
      print(f"turn {cup_game.turn}")  
  print(cup_game.part_two_ans())



if __name__ == '__main__':
  main()
