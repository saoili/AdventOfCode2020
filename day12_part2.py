FILENAME = 'day12_part1_eg1.txt'
# FILENAME = 'day12_part1_eg2.txt'
FILENAME = 'day12_part1.txt'
# FILENAME = 'day12_part2_eg.txt'


LEFT_OF = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}
RIGHT_OF = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}


class Ship():
  def __init__(self):
    self.direction = 'E'
    self.x = 0
    self.y = 0
    self.way_x = 10
    self.way_y = -1

  def move_right_once(self):
    # what was east is south
    # what was south is west
    # what was west is north
    # what was north is east
    # what was positive x is positive y
    # what was negative x is negative y
    # what was positive y is negative x
    # what was negative y is positive x
    old_x = self.way_x
    old_y = self.way_y

    self.way_y = old_x
    self.way_x = -old_y

  def move_left_once(self):
    # what was east is north
    # what was north is west
    # what was west is south
    # what was south is east
    # what was positive x is negative y
    # what was negative x is positive y
    # what was negative y is negative x
    # what was positive y is positive x
    old_x = self.way_x
    old_y = self.way_y

    self.way_y = -old_x
    self.way_x = old_y


  def move_left(self, degrees):
    while degrees > 0:
      self.move_left_once()
      degrees -= 90

  def move_right(self, degrees):
    while degrees > 0:
      self.move_right_once()
      degrees -= 90

  def move_north(self, distance):
    self.way_y -= distance

  def move_south(self, distance):
    self.way_y += distance

  def move_east(self, distance):
    self.way_x += distance

  def move_west(self, distance):
    self.way_x -= distance

  def move_forward(self, distance):
    self.x += distance * self.way_x
    self.y += distance * self.way_y

  def process_instruction(self, instruction, distance):
    if instruction == 'L':
      self.move_left(distance)
    if instruction == 'R':
      self.move_right(distance)
    if instruction == 'N':
      self.move_north(distance)
    if instruction == 'S':
      self.move_south(distance)
    if instruction == 'E':
      self.move_east(distance)
    if instruction == 'W':
      self.move_west(distance)
    if instruction == 'F':
      self.move_forward(distance)

  def __str__(self):
    return f"Pointing {self.direction} as {self.x, self.y} waypoint {self.way_x, self.way_y}"



def get_manhattan_from_origin(x, y):
  return abs(x) + abs(y)


def get_instructions():
  instructions = []

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      if line:
        instructions.append((line[0], int(line[1:])))

  return instructions


def main():
  instructions = get_instructions()
  print(instructions)
  ship = Ship()
  print(ship)
  for instruction in instructions:
    print(instruction, end=": ")
    ship.process_instruction(*instruction)
    print(ship)

  print(get_manhattan_from_origin(ship.x, ship.y))


if __name__ == '__main__':
  main()