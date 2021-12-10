# FILENAME = 'day3_part1_eg1.txt'
# FILENAME = 'day3_part1_eg2.txt'
FILENAME = 'day3_part1.txt'


def get_grid_from_file():
  trees = {}
  width = None
  height = 0

  with open(FILENAME, 'r') as file:
    for y, row in enumerate(file):
      height += 1
      if width is None:
        width = len(row)
      for x, value in enumerate(row):
        if value == '#':
          trees[(x, y)] = True

  return trees, width, height


def get_three_by_one(trees, width, height, right, down):
  x = 0
  y = 0
  num_trees = 0

  while y < height:
    x = (x + right) % (width - 1) 
    y += down
    # print(f"checking if tree at {x, y}", end="")
    if trees.get((x, y), False):
      num_trees += 1
    #   print(f" and there is")
    # else:
    #   print(f" and there isn't")

  return num_trees



def main():
  trees, width, height = get_grid_from_file()
  # print(trees)
  # print(width)
  # print(height)
  ans = 1

  for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    local_ans = get_three_by_one(trees, width, height, right, down)
    print(f"for {right, down} we get {local_ans}")
    ans *= local_ans

  print(ans)


if __name__ == '__main__':
  main()