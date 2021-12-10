from collections import defaultdict


FILENAME = 'day24_part1_eg1.txt'
FILENAME = 'day24_part1.txt'


def get_directions():
  directions = []

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      
      if not line:
        continue

      directions.append(line)

  return [parse_directions(d) for d in directions]


def parse_directions(directions):
  parsed_directions = []

  skip_next = False

  for i, char in enumerate(directions):
    # print(f"i is {i}, char is {char}")
    if skip_next:
      skip_next = False
      continue
    if char in ['s', 'n']:
      parsed_directions.append(char + directions[i+1])
      skip_next = True
    else:
      parsed_directions.append(char)

  # print(f"parsed_directions is {parsed_directions}")
  return parsed_directions


def move(x, y, direction):
  # print(f"moving from {x, y} in direction {direction}")
  if direction == 'w':
    return x+1, y
  if direction == 'e':
    return x-1, y
  if direction == 'nw':
    return x+1, y-1
  if direction == 'ne':
    return x, y-1
  if direction == 'sw':
    return x, y+1
  if direction == 'se':
    return x-1, y+1

  # print(f"I don't know how to go {direction}")


def flip_at(grid, directions):
  x, y = 0, 0

  for direction in directions:
    x, y = move(x, y, direction)
  
  # print(f"flipping at grid {x, y}")
  grid[(x, y)] = not grid.get((x, y))


def get_black_neighbours(tile, grid):
  black_neighbours = 0
  x, y = tile

  # print(f"getting black_neighbours for {tile} in grid {grid}")
  # print(f"getting black_neighbours for {tile}")

  for direction in (
    (x+1, y), (x-1, y), (x+1, y-1), (x, y-1), (x, y+1), (x-1, y+1),):
    if grid.get(direction):
      # print(f"{direction} is black")
      black_neighbours += 1
    # else:
    #   print(f"{direction} is not black")

  return black_neighbours


def tick(grid):
  old_grid = grid.copy()

  for x, y in grid.keys():
    for direction in (
      (x+1, y), (x-1, y), (x+1, y-1), (x, y-1), (x, y+1), (x-1, y+1),):
      old_grid[direction] = grid.get(direction)

  for tile, is_black in old_grid.items():
    black_neighbours = get_black_neighbours(tile, old_grid)
    if is_black and (black_neighbours == 0 or black_neighbours > 2):
      # print(f"{tile} is black and has {black_neighbours} black neighbours, so goes white")
      grid[tile] = False
    elif not is_black and black_neighbours == 2:
      # print(f"{tile} is white and has {black_neighbours} black neighbours, so goes black")
      grid[tile] = True
    # else:
    #   print(f"{tile} is black? {is_black} and has {black_neighbours} black_neighbours so doesn't change")


def main():
  directions = get_directions()
  # print(directions)
  grid = defaultdict(bool)
  # print(sum([1 for i in grid.keys() if i]))
  for direction in directions:
    flip_at(grid, direction)

  # print(grid)
  # print(sum([1 for i in grid.values() if i]))
  
  print(f"grid before ticking is")
  for location, value in grid.items():
    if value:
      print(f"{location} is black")

  for i in range(100):      
    tick(grid)
    print(sum([1 for i in grid.values() if i]))


if __name__ == '__main__':
  main()