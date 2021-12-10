class Game():
  def __init__(self, numbers):
    self.when_said_before_last = {}
    self.turn = len(numbers)
    self.last_number = numbers[-1]

    for i, number in enumerate(numbers):
      self.when_said_before_last[number] = i + 1

  def say_number(self):

    wsbl = self.when_said_before_last.get(self.last_number)

    if wsbl is None:
      this_number = 0
    else:
      # it's last turn really
      this_number = self.turn - wsbl

    # again, it's really last turn
    self.when_said_before_last[self.last_number] = self.turn

    self.last_number = this_number
    self.turn += 1

    # print(f"turn: {self.turn} saying {this_number}")

    return self.turn, this_number


def get_answer(numbers):
  game = Game(numbers)

  play_to = 2020
  turn = 0

  while turn < play_to:
    turn, this_number = game.say_number()

  return(this_number)


def main():
  for numbers in (
    (0,3,6,),
    (1,3,2,),
    (2,1,3,),
    (1,2,3,),
    (2,3,1,),
    (3,2,1,),
    (3,1,2,),
    (8,11,0,19,1,2),
  ):
    print(numbers)
    print(get_answer(numbers))


  


if __name__ == '__main__':
  main()