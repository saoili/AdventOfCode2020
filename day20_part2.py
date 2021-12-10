import math


FILENAME = 'day20_part1_eg1.txt'
FILENAME = 'day20_part1.txt'

# FILENAME = 'day20_part1_eg2.txt'
# FILENAME = 'day20_part2.txt'
# FILENAME = 'day20_part2_eg1.txt'
# FILENAME = 'day20_part2_eg2.txt'


SIZE = 10
SIZE_WITHOUT_BORDERS = 8
MONSTER_SPOTS = []
monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
for y, row in enumerate(monster.split("\n")):
  for x, char in enumerate(row):
    if char == '#':
      MONSTER_SPOTS.append((x, y))

MONSTER_HEIGHT = len(monster.split("\n"))
MONSTER_WIDTH = len(monster.split("\n")[0])
HASHES_PER_MONSTER = monster.count('#')


class Tile():
  def __init__(self, tile_number, tile_dict):
    self.number = tile_number
    self._dict = tile_dict
    self.fixed = False
    self.reset()
    self.borders_stripped = False
    self.size = SIZE

  def reset(self):
    self._top = None
    self._bottom = None
    self._left = None
    self._right = None

  def get_x_and_y(self):
    l = list(self._dict.values())
    len_l0 = len(l)
    return len_l0, len(self._dict.keys())

  def __str__(self):
    # print("in str")
    ret_val = []
    # ret_val.append(f"Tile: {self.number}")

    for y in range(self.size):
      row = self.get_row(y)
      ret_val.append(row)

    # ret_val.append("\n")
    return "\n".join(ret_val)

  def get_row(self, y):
    row = []
    for x in range(self.size):
      char_at = self._dict.get((x, y))
      if char_at is None:
        continue
      row.append(char_at)
    return "".join(row)

  @property
  def top(self):
    if self._top is None:
      self._top = "".join([self._dict[(x, 0)] for x in range(self.size)])
    return self._top
  
  @property
  def bottom(self):
    if self._bottom is None:
      self._bottom = "".join([self._dict[(x, self.size-1)] for x in range(self.size)])
    return self._bottom
  
  @property
  def left(self):
    if self._left is None:
      self._left = "".join([self._dict[(0, y)] for y in range(self.size)])
    return self._left
  
  @property
  def right(self):
    if self._right is None:
      self._right = "".join([self._dict[(self.size-1), y] for y in range(self.size)])
    return self._right
  
  def tops_and_bottoms(self):
    top = self.top
    bottom = self.bottom

    return [top, top[::-1], bottom, bottom[::-1]]

  def lefts_and_rights(self):
    left = self.left
    right = self.right

    return [left, left[::-1], right, right[::-1]]

  def all_sides_all_directions(self):
    return self.tops_and_bottoms() + self.lefts_and_rights()

  def rotate_or_flip_to_fit_to_right(self, tile2):
    # print(f"in rotate_or_flip_to_fit_to_right of {self.number} with {tile2.number}")
    if tile2.right == self.left:
      return

    # there are 8 possible positions
    # 1 is base, or both flips and 2 rotations
    # 2 is flipped top to bottom, or flipped left to right and 2 rotations
    # 3 is flipped left to right, or flipped top to bottom and 2 rotations
    # 4 is both flipped, or 2 rotations
    # 5 is 1 rotation or both flipped and 3 roations
    # 6 is flipped left to right and 1 rotation or flipped top to bottom and 3 rotations
    # 7 is flipped left to right and 3 rotations or flipped top to bottom and 1 rotation
    # 8 is 3 rotations or both flips and 1 rotation
    # we can hit all of these with 3 rotations, 1 flip, 3 more rotations
    # 1 -> 5 -> 4 -> 8 then either 3 -> 6 -> 2 -> 7 or 2 -> 7 -> 3 -> 6 depending on flip

    actions = [self.rotate]*3 + [self.flip_left_right] + [self.rotate]*3

    for action in actions:
      action()
      if tile2.right == self.left:
        return

    raise Exception(
      "rotate_and_flip_to_fit_to_right is only supposed to be used in"
      " cases where we know it fits some way around")

  def rotate_or_flip_to_fit_to_bottom(self, tile2):
    if tile2.bottom == self.top:
      return

    actions = [self.rotate]*3 + [self.flip_left_right] + [self.rotate]*3

    for action in actions:
      action()
      if tile2.bottom == self.top:
        return

    raise Exception(
      "rotate_and_flip_to_fit_to_bottom is only supposed to be used in"
      " cases where we know it fits some way around")


  # pretty as this is, we need to know what's inside, actually
  # def flip_left_right(self):
  #   self._left, self._right = self._right, self._left
  #   self._top, self._bottom = self._top[::-1], self._bottom[::-1]

  # def flip_top_botom(self):
  #   self._top, self._bottom = self._bottom, self._top
  #   self._left, self._right = self._left[::-1], self._right[::-1]

  # def rotate(self):
  #   (self._right, self._bottom, self._left, self._top) = (
  #     self._top, self._right[::-1], self._bottom, self._left[::-1])

  def flip_left_right(self):
    if self.fixed == True:
      print(f"Trying to flip_left_right {self.number} but it's already in!")
      return
    self.reset()
    old_dict = self._dict.copy()

    for y in range(self.size):
      for x in range(self.size):
        char_at = old_dict.get((x, y))
        new_x = self.size - x - 1
        new_y = y
        self._dict[(new_x, new_y)] = char_at
  
  def flip_top_bottom(self):
    if self.fixed == True:
      print(f"Trying to flip_top_bottom {self.number} but it's already in!")
      return
    self.reset()
    old_dict = self._dict.copy()

    for y in range(self.size):
      for x in range(self.size):
        char_at = old_dict.get((x, y))
        new_x = x
        new_y = self.size - y - 1
        self._dict[(new_x, new_y)] = char_at
  
  def rotate(self):
    if self.fixed == True:
      print(f"Trying to rotate {self.number} but it's already in!")
      return
    self.reset()
    old_dict = self._dict.copy()

    for a in range(self.size):
      for b in range(self.size):
        old_x = a
        old_y = self.size - b - 1
        char_at = old_dict.get((old_x, old_y))
        new_x = b
        new_y = a
        self._dict[(new_x, new_y)] = char_at

  def strip_borders(self):
    self.borders_stripped = True
    self.size = SIZE_WITHOUT_BORDERS
    old_dict = self._dict.copy()
    self._dict = {}

    for y in range(SIZE):
      for x in range(SIZE):
        border_numbers = [0, SIZE-1]
        if x in border_numbers or y in border_numbers:
          continue
        self._dict[(x-1, y-1)] = old_dict[(x, y)]


def can_match_top_to_bottom(tile1, tile2):
  top1 = tile1.top
  top2 = tile2.top
  bottom1 = tile1.bottom
  bottom2 = tile2.bottom

  for tile2_side in (top2, top2[::-1], bottom2, bottom2[::-1]):
    for tile1_side in (top1, bottom1):
      # I THINK trying its reverse would be duplication
      if tile1_side == tile2_side:
        # print(f"because {tile1_side} == {tile2_side}")
        return True

  return False


def can_match_on_right(tile1, tile2):
  right1 = tile1.right
  left2 = tile2.left

  if right1 == left2:
    return True

  flipped_left_right = tile2.copy()


  for tile2_side in (left2, left2[::-1], right2, right2[::-1]):
    for tile1_side in (left1, right1):
      # I THINK trying its reverse would be duplication
      if tile1_side == tile2_side:
        # print(f"because {tile1_side} == {tile2_side}")
        return True

  return False


def can_match_top(tile1, tile2):
  top1 = tile1.top
  top2 = tile2.top
  bottom2 = tile2.bottom

  for tile2_side in tile2.all_sides_all_directions():
    # I THINK trying its reverse would be duplication
    if top1 == tile2_side:
      # print(f"because {top1} == {tile2_side}")
      return True

  return False


def can_match_bottom(tile1, tile2):
  bottom1 = tile1.bottom
  top2 = tile2.top
  bottom2 = tile2.bottom

  for tile2_side in tile2.all_sides_all_directions():
    # I THINK trying its reverse would be duplication
    if bottom1 == tile2_side:
      # print(f"because {bottom1} == {tile2_side}")
      return True

  return False


def can_match_left(tile1, tile2):
  left1 = tile1.left
  left2 = tile2.left
  right2 = tile2.right

  for tile2_side in tile2.all_sides_all_directions():
    # I THINK trying its reverse would be duplication
    if left1 == tile2_side:
      # if tile1.number == 1489:
      #   print(f"returning true from can_match_left for {tile2.number} because {left1} == {tile2_side}")
      return True

  return False


def can_match_right(tile1, tile2):
  # if tile1.number == 1489:
  #   print(f"tile2 is {tile2.number}")

  right1 = tile1.right
  left2 = tile2.left
  right2 = tile2.right

  for tile2_side in tile2.all_sides_all_directions():
    # if tile1.number == 1427:
    #   print(f"tile2 is {tile2_side} (and right1 is {right1})")

    # I THINK trying its reverse would be duplication
    if right1 == tile2_side:
      # if tile1.number == 1489:
      #   print(f"because {right1} == {tile2_side}")
      return True
    # elif tile1.number == 1489 and tile2.number == 1171:
    #   print(f"tile2_side is {tile2_side}, which doesn't match {right1}")

  return False
  # right1 = tile1.right
  # left2 = tile2.left
  # right2 = tile2.right

  # for tile2_side in tile2.all_sides_all_directions():
  #   # I THINK trying its reverse would be duplication
  #   if right1 == tile2_side:
  #     # print(f"because {right1} == {tile2_side}")
  #     return True

  # return False


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


def wants_to_be_where(tile, tiles):
  has_match_above = can_have_above(tile, tiles)
  has_match_left = can_have_left(tile, tiles)
  above_or_below = 'bottom' if has_match_above else 'top'
  left_or_right = 'right' if has_match_left else 'left'

  # print(f"tile {tile.number} wants to be in the {above_or_below} {left_or_right} corner")
  return above_or_below, left_or_right


def rotate_or_flip_to_top_left(first_corner, tiles):
  above_or_below, left_or_right = wants_to_be_where(first_corner, tiles)
  if above_or_below == 'bottom':
    if left_or_right == 'right':
      first_corner.rotate()
      first_corner.rotate()
    else:
      first_corner.flip_top_bottom()
  else:
    if left_or_right == 'right':
      first_corner.flip_left_right()

  above_or_below, left_or_right = wants_to_be_where(first_corner, tiles)


class Grid():
  def __init__(self, tiles):
    self.tiles = tiles
    self.image = {}
    self.image_options = {}
    self.image_width = int(math.sqrt(len(tiles)))
    self.complete = False
    self.corners = []
    self.edges = []
    self.middles = []
    self.borders_stripped = False
    
    for tile_number, tile in self.tiles.items():
      top_or_bottom = (not can_have_above(tile, self.tiles)) or (not can_have_below(tile, self.tiles))
      side = (not can_have_left(tile, self.tiles)) or (not can_have_right(tile, self.tiles))

      if top_or_bottom and side:
        # print(f"adding tile {tile.number} to corners")
        self.corners.append(tile)
      elif top_or_bottom or side:
        # print(f"adding tile {tile.number} to edges")
        self.edges.append(tile)
      else:
        # print(f"adding tile {tile.number} to middles")
        self.middles.append(tile)

      # if tile_number == 1489:
      #   print(f"can_have_above(tile_number) is {can_have_above(tile, tiles)}")
      #   print(f"can_have_below(tile_number) is {can_have_below(tile, tiles)}")
      #   print(f"can_have_left(tile_number) is {can_have_left(tile, tiles)}")
      #   print(f"can_have_right(tile_number) is {can_have_right(tile, tiles)}")
      #   print(f"top_or_bottom is {top_or_bottom}")
      #   print(f"side is {side}")
    
    print("before trying to fill")
    # print(f"here corners has {len(self.corners)}")
    # print(f"here edges has {len(self.edges)}")
    # print(f"here middles has {len(self.middles)}")

    self.fill()

  def place(self, tile, location, source):
    print(f"placing {tile.number} at {location}")
    x, y = location
    can_go_there = self.image_options.get(location)
    
    if can_go_there is not None:
      if tile.number not in can_go_there:
        raise Exception(f"Trying to put tile {tile.number} as {location} but can't")

    if y == 0:
      if x != 0:  # if it is we've done the work in 'place_top_left'
        fit_right_of = self.image[(x-1, y)]
        print(f"trying to put {tile.number} to the right of {fit_right_of.number}")
        tile.rotate_or_flip_to_fit_to_right(fit_right_of)
    else:
      fit_below = self.image[(x, y-1)]
      print(f"trying to put {tile.number} below {fit_below.number}")
      tile.rotate_or_flip_to_fit_to_bottom(fit_below)

    self.image_options[location] = [tile.number]
    self.image[location] = tile
    tile.fixed = True
    source.remove(tile)

  def place_top_left(self):
    top_or_bottom = False
    side = True

    first_corner = self.corners[0]

    rotate_or_flip_to_top_left(first_corner, self.tiles)
    self.place(first_corner, (0, 0), self.corners)

  def __str__(self):
    if self.borders_stripped:
      size = SIZE_WITHOUT_BORDERS
    else:
      size = SIZE

    rows = []

    for grid_y in range(self.image_width):
      these_tiles = []
      for grid_x in range(self.image_width):
        these_tiles.append(self.image.get((grid_x, grid_y)))
        # for i in range(SIZE_WITHOUT_BORDERS):
        #   print(these_tiles[-1].get_row(i))
      
      for tile_y in range(size):
        row = []
        for tile in these_tiles:
          row.append(tile.get_row(tile_y))
        rows.append("".join(row))

    return "\n".join(rows)

    # for y in range(SIZE * self.image_width):
    #   y_in_tile = y % SIZE
    #   for i in range(self.image_width):


    #   for x in range(SIZE * self.image_width):
    #     x_in_tile = x % SIZE


    #   def __str__(self):
    # # print("in str")
    # ret_val = []
    # # ret_val.append(f"Tile: {self.number}")

    # for y in range(SIZE):
    #   row = []
    #   for x in range(SIZE):
    #     char_at = self._dict.get((x, y))
    #     # print(f"character at {x, y} is {char_at}")
    #     if char_at is None:
    #       continue
    #     row.append(char_at)
    #   ret_val.append("".join(row))

    # # ret_val.append("\n")
    # return "\n".join(ret_val)



    # rows = []

    # for y in range(self.image_width):
    #   row = []
    #   for x in range(self.image_width):
    #     row.append(str(self.image.get((x, y))))
    #   rows.append("".join(row))

    # rows.append("".join(row))

    # return "\n".join(rows)

  def try_to_place_at(self, x, y):
    print(f"trying to place at {x, y}")

    at_top = y == 0
    at_bottom = y == self.image_width - 1
    at_left = x == 0
    at_right = x == self.image_width - 1

    if at_top and at_left:
      self.place_top_left()
      print("placed at top left")
      return

    if (at_top or at_bottom) and (at_left or at_right):
      source = self.corners
    elif at_top or at_bottom or at_right or at_left:
      source = self.edges
    else:
      source = self.middles

    if not at_top:
      # must match the thing above it
      tile_above = self.image.get((x, y-1))

      # uncomment in case of emergeny
      # if tile_above is None:
      #   possible_tiles_above = self.image_options.get((x, y-1))
      # else:
      #   possible_tiles_above = [tile_above]
      print(f"seeing if any of these {len(source)} tiles fit below what's in {x, y-1}")
      if tile_above is not None:
        print(f"which is {tile_above.number}")

      can_fit_below = set()

      for tile2 in source:
        if can_match_bottom(tile_above, tile2):
          can_fit_below.add(tile2.number)
      # print("".join([str(t) for t in source]))
      # print(len(source))
    else:
      can_fit_below = set([tile.number for tile in source])

    if not at_left:
      # must match the thing to the left of it
      tile_left = self.image.get((x-1, y))
      print(f"seeing if any of these {len(source)} tiles fit right of what's in {x-1, y}")
      if tile_left is not None:
        print(f"which is\n{tile_left.number}")

      can_fit_right_of = set()

      for tile2 in source:
        if can_match_right(tile_left, tile2):
          can_fit_right_of.add(tile2.number)

      # print("".join([str(t) for t in source]))
      # print(len(source))
    else:
      can_fit_right_of = set([tile.number for tile in source])

    can_fit_both = can_fit_below.intersection(can_fit_right_of)

    if len(can_fit_both) == 1:
      tile_number = list(can_fit_both)[0]
      print(f"Hurrah, only tile {tile_number} can go there")
      tile = self.tiles[tile_number]
      self.place(tile, (x, y), source)
    else:
      print(f"Dang, not sure I've fully allowed for that")
      self.image_options[(x, y)] = can_fit_both


  def fill(self):
    for y in range(self.image_width):
      for x in range(self.image_width):
        self.try_to_place_at(x, y)

  def strip_borders(self):
    for tile in self.tiles.values():
      tile.strip_borders()
      self.borders_stripped = True

  def flip_left_right(self):
    old_image = self.image.copy()

    for y in range(self.image_width):
      for x in range(self.image_width):
        tile_at = old_image.get((x, y))
        new_x = self.image_width - x - 1
        new_y = y
        tile_at.fixed = False
        tile_at.flip_left_right()
        self.image[(new_x, new_y)] = tile_at
  
  def rotate(self):
    old_image = self.image.copy()

    for a in range(self.image_width):
      for b in range(self.image_width):
        old_x = a
        old_y = self.image_width - b - 1
        tile_at = old_image.get((old_x, old_y))
        tile_at.fixed = False
        tile_at.rotate()
        new_x = b
        new_y = a
        self.image[(new_x, new_y)] = tile_at

  def set_full_image(self):
    image = str(self)
    self.full_image_grid = {}

    for y, row in enumerate(image.split("\n")):
      for x, char in enumerate(row):
        self.full_image_grid[(x, y)] = char

    return self.full_image_grid

  def monster_at(self, x, y, debug=False):
    for mx, my in MONSTER_SPOTS:
      if debug:
        print(f"x is {x}, mx is {mx}, y is {y}, my is {my}")
        print(f"x+mx is {x+mx}, y+my is {y+my}")
        print(f"self.full_image_grid[(x+mx, y+my)] is {self.full_image_grid[(x+mx, y+my)]}")
      if not self.full_image_grid[(x+mx, y+my)] == '#':
        if debug:
          print(self)
        return False
    return True

  def _current_monster_count(self, debug=False):
    full_size = SIZE_WITHOUT_BORDERS * self.image_width
    monsters = 0

    for y in range(full_size - MONSTER_HEIGHT):
      for x in range(full_size - MONSTER_WIDTH):
        # print(f"check starting at {x, y}")
        # print(self.full_image_grid[x+MONSTER_WIDTH, y+MONSTER_HEIGHT])
        # if debug:
        #   print(f"self.monster_at{x, y} is {self.monster_at(x, y)}")
        if self.monster_at(x, y, debug and x==2 and y==2):
          monsters += 1
     
    return monsters
  
  def monster_count(self):
    self.set_full_image()
    current = self._current_monster_count()

    print(f"before any actions, found {current} monsters")

    if current > 0:
      return current

    actions = [self.rotate]*3 + [self.flip_left_right] + [self.rotate]*3

    for i, action in enumerate(actions):
      self.set_full_image()
      action()      
      current = self._current_monster_count(i==5)
      print(f"\nafter {i+1} actions")
      # print(f"grid is\n{self}")
      print(f"found {current} monsters")
      if current > 0:
        return current

    return -1

  def get_roughness(self):
    monsters = self.monster_count()
    total_hashes = str(self).count('#')

    return total_hashes - monsters * HASHES_PER_MONSTER


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
  print(tiles)
  grid = Grid(tiles)
  print(grid)
  grid.strip_borders()
  print("\nAnd after stripping borders")
  print(grid)

  print("\n")

  # print(grid.monster_count())

  print(grid.get_roughness())


  

if __name__ == '__main__':
  main()