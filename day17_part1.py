from collections import defaultdict

FILENAME = 'day17_part1_eg1.txt'
# FILENAME = 'day17_part1_eg2.txt'
FILENAME = 'day17_part1.txt'
# FILENAME = 'day17_part2_eg.txt'


class Dimension():
  def __init__(self, lines):
    self.min_z = 0
    self.max_z = 0
    self.min_x = 0
    self.max_x = len(lines[0]) - 1
    self.min_y = 0
    self.max_y = len(lines) - 1
    self.co_ords = defaultdict(bool)

    z = 0

    for y, line in enumerate(lines):
      for x, char in enumerate(line):
        if char == '#':
          self.co_ords[(x, y, z)] = True

  def __str__(self):
    all_layers = ["\n"]

    for z in range(self.min_z, self.max_z+1):
      layer = [f"\nLayer at z {z}"]
      for y in range(self.min_y, self.max_y+1):
        row = []
        for x in range(self.min_x, self.max_x+1):
          # if (x, y, z) == 
          if self.co_ords[(x, y, z)]:
            row.append('#')
          else:
            row.append('.')
        row.append(f'    ({y})')
        blah = "".join(row) 
        layer.append("".join(row))
      all_layers.append("\n".join(layer))

    return "\n".join(all_layers)

  def get_active_neighbours(self, x, y, z):
    active_neighbours = 0

    for zi in range(z-1, z+2):
      for yi in range(y-1, y+2):
        for xi in range(x-1, x+2):
          if zi == z and xi == x and yi == y:
            continue
          if self.last_co_ords[(xi, yi, zi)]:
            # if (x, y, z) == (-1, 1, 0):
            #   print(f"{xi, yi, zi} is active")
            active_neighbours += 1

    return active_neighbours

  def tick(self):
    self.last_co_ords = self.co_ords.copy()

    for z in range(self.min_z-1, self.max_z+2):
      # print("\n")
      for y in range(self.min_y-1, self.max_y+2):
        # print()
        for x in range(self.min_x-1, self.max_x+2):
          active_neighbours = self.get_active_neighbours(x, y, z)
          active = self.co_ords[(x, y, z)]
          # print(f"{x, y, z} is active: {active} and has {active_neighbours} active_neighbours", end=" ")
          if (
            (active and active_neighbours in (2, 3)) or
            (not active and active_neighbours == 3)
          ):
            self.co_ords[(x, y, z)] = True
            self.min_z = min(self.min_z, z)
            self.max_z = max(self.max_z, z)
            self.min_x = min(self.min_x, x)
            self.max_x = max(self.max_x, x)
            self.min_y = min(self.min_y, y)
            self.max_y = max(self.max_y, y)
            # print("setting active")
          else:
            self.co_ords[(x, y, z)] = False
            # print("setting inactive")

  def count_active(self):
    active = 0

    for active_value in self.co_ords.values():
      if active_value:
        active += 1

    return active


def get_lines():
  lines = []

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      if not line:
        continue

      lines.append(line)

  return lines



def main():
  lines = get_lines()
  dimension = Dimension(lines)
  print(dimension)

  for i in range(6):
    dimension.tick()

  print(dimension.count_active())


  # print(f"dimension.min_z is {dimension.min_z}")
  # print(f"dimension.max_z is {dimension.max_z}")
  # print(f"dimension.min_x is {dimension.min_x}")
  # print(f"dimension.max_x is {dimension.max_x}")
  # print(f"dimension.min_y is {dimension.min_y}")
  # print(f"dimension.max_y is {dimension.max_y}")



if __name__ == '__main__':
  main()