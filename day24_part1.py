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


def main():
  directions = get_directions()
  # print(directions)
  grid = defaultdict(bool)
  # print(sum([1 for i in grid.keys() if i]))
  for direction in directions:
    flip_at(grid, direction)

  # print(grid)
  print(sum([1 for i in grid.values() if i]))
  


if __name__ == '__main__':
  main()