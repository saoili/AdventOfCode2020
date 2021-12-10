class BootCodeReader():
  def __init__(self, filename):
    self.accumulator = 0
    self.index = 0
    self.debug = False
    self.visited_indexes = []
    self.terminated = False

    self.fill_from_file(filename)

  def reset(self):
    self.accumulator = 0
    self.index = 0
    self.visited_indexes = []
    self.terminated = False

  def fill_from_file(self, filename):
    self.instructions = []

    with open(filename, 'r') as file:
      for line in file:
        line = line.strip()

        op, arg = line.split()
        arg = int(arg)

        self.instructions.append((op, arg))

  def acc(self, number):
    self.accumulator += number
    self.index += 1

  def jmp(self, number):
    self.index += number

  def nop(self, number):
    self.index += 1

  def tick(self):
    if self.debug:
      print(f"ticking from index {self.index} and accumulator {self.accumulator}")

    op, number = self.instructions[self.index]
    if op == 'acc':
      self.acc(number)
    if op == 'jmp':
      self.jmp(number)
    if op == 'nop':
      self.nop(number)

    if self.debug:
      print(f"op was {op}, number was {number}")
      print(f"ticked to index {self.index} and accumulator {self.accumulator}")

    if self.index == len(self.instructions):
      self.terminated = True

      if self.debug:
        print(f"self.index is len instructions, terminating")

  def accumulator_before_repeat(self):
    while self._keep_going():
      self.visited_indexes.append(self.index)
      self.tick()

    return self.accumulator

  def _keep_going(self):
    if self.index in self.visited_indexes:
      return False

    return True

  def terminates(self):
    while self._keep_going() and not self.terminated:
      self.visited_indexes.append(self.index)
      self.tick()

    return self.terminated
