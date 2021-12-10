INPUT_EG1 = "389125467"
INPUT = "962713854"


class Cup():
  def __init__(self, value):
    self.value = value
    self.to_the_right = None
    self.to_the_left = None

  def __str__(self):
    # return f"cup with value {self.value}"
    return str(self.value)


class CupGame():
  def __init__(self, cups_string):
    # print(f"cups_string is {cups_string}")
    self.cups = set()
    self.current_cup = None
    self.size = len(cups_string)
    self.turn = 0


    all_lables = list(cups_string) + list(range(self.size, 1000001))

    for i in all_lables:
      # print(f"i is {i}")
      c = Cup(int(i))
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



    # print(f"last c is {c}")
    # print(f"setting {self.current_cup.value} as to the right of {c.value}")
    # print(f"and {c.value} as to the right of {self.current_cup}")
    c.to_the_right = self.current_cup
    self.current_cup.to_the_left = c

    # print(f"self.cups is {[str(c) for c in self.cups]}")
    # print(f"with len {len(self.cups)}")

  # def take_turn(self):
  #   cups_out = self.cups[self.current_index+1: self.current_index+4]
  #   cups_left = self.cups[:self.current_index] + self.cups[self.current_index+4:]

  def __str__(self):
    ret_val = ""

    for cup in self.cups:
      if cup.value == 1:
        one_cup = cup
        break
      # else:
      #   print(f"cup.value is {cup.value}")

    # print(f"one_cup is {one_cup}")
    next_cup = one_cup.to_the_right
    # print(f"next_cup is {next_cup}")

    for i in range(self.size-1):
      # print(f"the next cup is {next_cup.to_the_right}")
      ret_val = ret_val + str(next_cup.value)
      next_cup = next_cup.to_the_right

    return ret_val

  def take_turn(self, prints=False):
    self.turn += 1
    if prints:
      print(f"-- move {self.turn} --")

    values = []
    current_print = self.start_print_at
    for i in range(self.size):
      if current_print == self.current_cup:
        values.append(f"({current_print})")
      else:
        values.append(str(current_print.value))
      current_print = current_print.to_the_right

    if prints:
      print(f"cups: {' '.join(values)}")


    first = self.current_cup.to_the_right
    second = first.to_the_right
    third = second.to_the_right
    forth = third.to_the_right

    # print(f"first has value {first.value}")
    # print(f"second has value {second.value}")
    # print(f"third has value {third.value}")

    if prints:
      print(f"pick up: {first}, {second}, {third}")

    self.current_cup.to_the_right = forth
    forth.to_the_left = self.current_cup

    first.to_the_left = None
    third.to_the_right = None

    destination_value = self.current_cup.value
    destination = None
    min_in_circle = None
    max_in_cirle = None

    for cup in self.cups:
      if cup in (first, second, third):
        continue
      if min_in_circle is None:
        min_in_circle = cup.value
        max_in_cirle = cup.value
      else:
        min_in_circle = min(min_in_circle, cup.value)
        max_in_cirle = max(max_in_cirle, cup.value)

    x = 0

    while destination is None and x < 3:
      x += 1
      destination_value -= 1
      if destination_value < min_in_circle:
        destination_value = max_in_cirle

      # print(f"Looking for a cup with value {destination_value}", end=" ")
      for cup in self.cups:
        if cup in (first, second, third):
          continue
        if cup.value == destination_value:
          # print("oh, we found it")
          destination = cup
          break
        # else:
        #   print(f"but this cup has value {cup.value}")

    # print(f"trying to put {first}{second}{third} in between {destination} and {destination.to_the_right}")
    if prints:
      print(f"destination: {destination}\n")

    to_the_right = destination.to_the_right

    third.to_the_right = to_the_right
    to_the_right.to_the_left = third

    first.to_the_left = destination
    destination.to_the_right = first

    self.current_cup = self.current_cup.to_the_right



def main():
  # cup_game = CupGame(INPUT_EG1)
  cup_game = CupGame(INPUT)
  print(cup_game)
  for i in range(100):
    cup_game.take_turn()  
  print(cup_game)



if __name__ == '__main__':
  main()
