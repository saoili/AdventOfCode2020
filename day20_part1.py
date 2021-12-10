import math


FILENAME = 'day22_part1_eg1.txt'
FILENAME = 'day22_part1.txt'

# FILENAME = 'day22_part1_eg2.txt'
# FILENAME = 'day22_part2.txt'
# FILENAME = 'day22_part2_eg1.txt'
# FILENAME = 'day22_part2_eg2.txt'


SIZE = 10


class Tile():
  def __init__(self, tile_number, tile_dict):
    self.number = tile_number
    self.dict = tile_dict

  def get_x_and_y(self):
    l = list(self.dict.values())
    len_l0 = len(l)
    return len_l0, len(self.dict.keys())

  def __str__(self):
    ret_val = []
    ret_val.append(f"Tile: {self.number}")

    for y in range(SIZE):
      row = []
      for x in range(SIZE):
        char_at = self.dict.get((x, y))
        if char_at is None:
          continue
        row.append(char_at)
      ret_val.append("".join(row))

    ret_val.append("\n")
    return "\n".join(ret_val)

  def get_top(self):
    return "".join([self.dict[(x, 0)] for x in range(SIZE)])

  def get_bottom(self):
    return "".join([self.dict[(x, SIZE-1)] for x in range(SIZE)])

  def get_left(self):
    return "".join([self.dict[(0, y)] for y in range(SIZE)])

  def get_right(self):
    return "".join([self.dict[(SIZE-1), y] for y in range(SIZE)])

  def all_sides_all_directions(self):
    top = self.get_top()
    bottom = self.get_bottom()
    left = self.get_left()
    right = self.get_right()

    ret_vals = []

    for side in top, bottom, left, right:
      ret_vals.append(side)
      ret_vals.append(side[::-1])

    return ret_vals


def can_match_top_to_bottom(tile1, tile2):
  top1 = tile1.get_top()
  top2 = tile2.get_top()
  bottom1 = tile1.get_bottom()
  bottom2 = tile2.get_bottom()

  for tile2_side in (top2, top2[::-1], bottom2, bottom2[::-1]):
    for tile1_side in (top1, bottom1):
      # I THINK trying its reverse would be duplication
      if tile1_side == tile2_side:
        # print(f"because {tile1_side} == {tile2_side}")
        return True

  return False


def can_match_side(tile1, tile2):
  left1 = tile1.get_left()
  left2 = tile2.get_left()
  right1 = tile1.get_right()
  right2 = tile2.get_right()

  for tile2_side in (left2, left2[::-1], right2, right2[::-1]):
    for tile1_side in (left1, right1):
      # I THINK trying its reverse would be duplication
      if tile1_side == tile2_side:
        # print(f"because {tile1_side} == {tile2_side}")
        return True

  return False


def can_match_top(tile1, tile2):
  top1 = tile1.get_top()
  top2 = tile2.get_top()
  bottom2 = tile2.get_bottom()

  for tile2_side in tile2.all_sides_all_directions():
    # I THINK trying its reverse would be duplication
    if top1 == tile2_side:
      # print(f"because {top1} == {tile2_side}")
      return True

  return False


def can_match_bottom(tile1, tile2):
  bottom1 = tile1.get_bottom()
  top2 = tile2.get_top()
  bottom2 = tile2.get_bottom()

  for tile2_side in tile2.all_sides_all_directions():
    # I THINK trying its reverse would be duplication
    if bottom1 == tile2_side:
      # print(f"because {bottom1} == {tile2_side}")
      return True

  return False


def can_match_left(tile1, tile2):
  left1 = tile1.get_left()
  left2 = tile2.get_left()
  right2 = tile2.get_right()

  for tile2_side in tile2.all_sides_all_directions():
    # I THINK trying its reverse would be duplication
    if left1 == tile2_side:
      # print(f"because {left1} == {tile2_side}")
      return True

  return False


def can_match_right(tile1, tile2):
  # if tile1.number == 1427:
  #   print(f"tile2 is {tile2.number}")

  right1 = tile1.get_right()
  left2 = tile2.get_left()
  right2 = tile2.get_right()

  for tile2_side in tile2.all_sides_all_directions():
    # if tile1.number == 1427:
    #   print(f"tile2 is {tile2_side} (and right1 is {right1})")

    # I THINK trying its reverse would be duplication
    if right1 == tile2_side:
      # print(f"because {right1} == {tile2_side}")
      return True

  return False


def can_have_above(tile1, tiles):
  for tile2 in tiles.values():
    if tile1 == tile2:
      continue
    if can_match_top(tile1, tile2):
      return True

  return False


def can_have_below(tile1, tiles):
  for tile2 in tiles.values():
    if tile1 == tile2:
      continue
    if can_match_bottom(tile1, tile2):
      return True

  return False


def can_have_left(tile1, tiles):
  for tile2 in tiles.values():
    if tile1 == tile2:
      continue
    if can_match_left(tile1, tile2):
      return True

  return False


def can_have_right(tile1, tiles):
  for tile2 in tiles.values():
    if tile1 == tile2:
      continue
    if can_match_right(tile1, tile2):
      return True

  return False


def get_tiles():
  tiles = {}
  tile = None

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      
      if not line:
        continue

      if 'Tile' in line:
        if tile is not None:
          tiles[tile_number] = Tile(tile_number, tile)

        tile_number = int(line.replace('Tile ', '').replace(':', ''))
        y = 0
        tile = {}
      else:
        for x, char in enumerate(line):
          tile[(x, y)] = char
        y += 1

  tiles[tile_number] = Tile(tile_number, tile)

  return tiles


def main():
  tiles = get_tiles()
  # for tile_number, tile in tiles.items():
  #   # print(f"tile {tile_number} is ")
  #   # print(tile.get_x_and_y())
  #   print(tile)

  # num_tiles = len(tiles.values())
  # print(f"there are {num_tiles} tiles")
  # print(f"making a grid with {math.sqrt(num_tiles)} tiles to a side")

  # print(can_match_side(tiles[1951], tiles[2311]))


  # print(f"can_match_top_to_bottom(tiles[1951], tiles[2311]) is {can_match_top_to_bottom(tiles[1951], tiles[2311])}")
  # print(f"can_match_top_to_bottom(tiles[1951], tiles[2311]) is {can_match_top_to_bottom(tiles[1951], tiles[2311])}")
  # print(f"can_match_top(tiles[1951], tiles[2729]) is {can_match_top(tiles[1951], tiles[2729])}")
  # print(f"can_match_top(tiles[2729], tiles[1951]) is {can_match_top(tiles[2729], tiles[1951])}")
  # print(f"\ncan_match_side(tiles[1951], tiles[2311]) is {can_match_side(tiles[1951], tiles[2311])}")
  # print(f"can_match_left(tiles[1951], tiles[2311]) is {can_match_left(tiles[1951], tiles[2311])}")
  # print(f"can_match_left(tiles[2311], tiles[1951]) is {can_match_left(tiles[2311], tiles[1951])}")
  # print(f"can_match_right(tiles[1951], tiles[2311]) is {can_match_right(tiles[1951], tiles[2311])}")
  # print(f"can_match_right(tiles[2311], tiles[1951]) is {can_match_right(tiles[2311], tiles[1951])}")

  top_or_bottom = False
  side = True
  corners = []
  corner_numbers = []
  answer = 1

  # for tile_number, tile in tiles.items():
  #   if not can_have_above(tile, tiles):
  #     print(f"tile {tile_number} is at the top, or at the bottom rotated or flipped")
  #   elif not can_have_below(tile, tiles):
  #     print(f"tile {tile_number} is at the bottom, or at the top rotated or flipped")

  #   if not can_have_left(tile, tiles):
  #     print(f"tile {tile_number} is at the left, or at the right rotated or flipped")
  #   elif not can_have_right(tile, tiles):
  #     print(f"tile {tile_number} is at the right, or at the left rotated or flipped")

  for tile_number, tile in tiles.items():
    if not can_have_above(tile, tiles) or not can_have_below(tile, tiles):
      print(f"tile {tile_number} is at the top or at the bottom (maybe rotated or flipped)")
      top_or_bottom = True
    else:
      top_or_bottom = False

    if not can_have_left(tile, tiles) or not can_have_right(tile, tiles):
      print(f"tile {tile_number} is at the left or at the right (maybe rotated or flipped)")
      side = True
    else:
      side = False

    if top_or_bottom and side:
      corners.append(tile)
      corner_numbers.append(str(tile.number))
      answer *= tile.number

  print(f"the corners are {', '.join(corner_numbers)}")
  print(f"the answer is {answer}")




if __name__ == '__main__':
  main()