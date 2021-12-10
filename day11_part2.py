FILENAME = 'day11_part1_eg1.txt'
# FILENAME = 'day11_part1_eg2.txt'
FILENAME = 'day11_part1.txt'
# FILENAME = 'day11_part2_eg.txt'


DIRECTION = (
  (-1, -1), (-1, 0), (-1, 1),
  (0, -1), (0, 1),
  (1, -1), (1, 0), (1, 1))


class Grid():
  def __init__(self, grid):
    self.grid = grid
    self.max_y = max([p[1] for p in self.grid.keys()])
    self.max_x = max([p[0] for p in self.grid.keys()])

  def __str__(self):
    ret_val = []
    for y in range(self.max_y + 1):
      this_row = []
      for x in range(self.max_x + 1):
        this_row.append(self.grid[(x, y)])
      ret_val.append("".join(this_row))

    return "\n".join(ret_val)

  def get_next_seat_occupied(self, from_location, direction):
    # if from_location in ((7, 7), (6, 6), (5, 5)):
    #   print(f"getting {from_location} in {direction}", end=" ")
    x, y = from_location
    x1, y1 = direction
    new_x = x + x1
    new_y = y + y1

    first_that_way = self.old_grid.get((new_x, new_y))

    if first_that_way in [None, 'L']:
      # if from_location in ((7, 7), (6, 6), (5, 5)):
      #   print(f"false because first_that_way at {new_x, new_y} is {first_that_way}")
      return False

    if first_that_way == '#':
      # if from_location in ((7, 7), (6, 6), (5, 5)):
      #   print(f"true becuase #")
      return True

    # if from_location in ((7, 7), (6, 6), (5, 5)):
    #   print(f"keep going from {(new_x, new_y)} in {direction}")
    return self.get_next_seat_occupied((new_x, new_y), direction)


  def count_neighbours(self, location):
    occupied_neighbours = 0
    new_occupied_neighbours = 0
    # print(f"count_neighbours for {location}")
    
    for direction in DIRECTION:
      if self.get_next_seat_occupied(location, direction):
        new_occupied_neighbours += 1

      current_x, current_y = location
      x1, y1 = direction

      while True:
        current_x += x1
        current_y += y1

        if not(0 <= current_x <= self.max_x and 0 <= current_y <= self.max_y):
          keep_looking = False  # I don't think I need this, but it's easier to read
          break

        neighbour_seat = self.old_grid.get((current_x, current_y))

        if neighbour_seat == '#':
          # if location == (7, 7):
          #   print(f"adding to occupied_neighbours because {current_x, current_y} is #")
          occupied_neighbours += 1
          break
        if neighbour_seat == 'L':
          break

    if new_occupied_neighbours != occupied_neighbours:
      print(f"they weren't the same for location {location}")
      print(f"new said {new_occupied_neighbours}, old said {occupied_neighbours}")

    return occupied_neighbours

  def tick(self):
    self.old_grid = self.grid.copy()

    for location, seat in self.grid.items():
      if seat == '.':
        continue

      occupied_neighbours = self.count_neighbours(location)

      if seat == 'L':
        if occupied_neighbours == 0:
          self.grid[location] = '#'
      if seat == '#':
        if occupied_neighbours >= 5:
          self.grid[location] = 'L'

    return self.old_grid == self.grid

  def count_occupied(self):
    total = 0

    for y in range(self.max_y + 1):
      for x in range(self.max_x + 1):
        if self.grid[(x, y)] == '#':
          total += 1

    return total


def get_grid():
  grid = {}

  lines = []

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      if line:
        lines.append(line)

  for y, line in enumerate(lines):
    for x, seat in enumerate(line):
      grid[(x, y)] = seat

  return grid


def main():
  grid = Grid(get_grid())

  # grid.tick()
  # print("\n"*50)
  # grid.tick()
  while not grid.tick():
    print()
    print(grid)
    pass

  # print()
  # print(grid)
  print(grid.count_occupied())


if __name__ == '__main__':
  main()