FILENAME = 'day11_part1_eg1.txt'
# FILENAME = 'day11_part1_eg2.txt'
FILENAME = 'day11_part1.txt'
# FILENAME = 'day11_part2_eg.txt'


NEIGHBOURS = (
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

  def count_neighbours(self, location):
    x, y = location
    occupied_neighbours = 0
    
    for x1, y1 in NEIGHBOURS:
      neighbour_x = x + x1
      neighbour_y = y + y1

      if 0 <= neighbour_x <= self.max_x and 0 <= neighbour_y <= self.max_y:
        neighbour_seat = self.old_grid.get((neighbour_x, neighbour_y))

        if neighbour_seat == '#':
          occupied_neighbours += 1

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
        if occupied_neighbours >= 4:
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

  while not grid.tick():
    pass

  print(grid.count_occupied())


if __name__ == '__main__':
  main()