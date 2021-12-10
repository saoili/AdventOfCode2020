from collections import defaultdict


FILENAME = 'day7_part1_eg.txt'
# FILENAME = 'day7_part1_eg2.txt'
FILENAME = 'day7_part1.txt'


class Bag():
  def __init__(self, name, sub_bags):
    self.name = name
    self.direct = defaultdict(int)
    self.indirect = defaultdict(int)
    self.add_sub_bags(sub_bags)

  def add_sub_bags(self, sub_bags):
    for number, bag in sub_bags:
      self.direct[bag] += number

  def contents_str(self):
    ret_str = ""

    for bag, number in self.direct.items():
      ret_str = ret_str + f"{number} {bag} "

    return ret_str.strip()

  def __str__(self):
    return f"{self.name} contains {self.contents_str()}\n"


def can_contain_gold(this_bag, all_bags):
  looking_for = 'shiny gold'

  if looking_for in this_bag.direct:
    return True

  for sub_bag_name in this_bag.direct:
    sub_bag = all_bags.get(sub_bag_name)

    if can_contain_gold(sub_bag, all_bags):
      return True

  return False


def get_outer_bags():
  outer_bags = {}

  with open(FILENAME, 'r') as file:
    for line in file:
      # print("\n\n")
      line = line.strip().replace(".", '')
      outer_bag, rest = line.split(' contain ')
      outer_bag = outer_bag.replace(' bags', '').replace(' bag', '')

      # print(f"outer_bag is {outer_bag}")
      # print(f"rest is {rest}")

      contents = []

      if rest != 'no other bags':
        raw_contents = rest.split(', ')
        # print(f"raw_contents is {raw_contents}")
        for bag in raw_contents:
          # print(f"bag is {bag}")
          number = int(bag[0])
          bags_in = bag[2:].replace(' bags', '').replace(' bag', '')
          contents.append((number, bags_in))

      outer_bags[outer_bag] = contents

  return outer_bags


def main():
  outer_bags = get_outer_bags()
  bags = {}

  for bag_name, contents in outer_bags.items():
    bags[bag_name] = Bag(bag_name, contents)

  total_can = 0

  for bag_name, bag in bags.items():
    # print(f"bag is {bag}", end="")
    can =can_contain_gold(bag, bags)
    # print(f"it can contain gold: {can}")
    # print("\n")
    if can:
      total_can += 1

  print(f"the total that can is {total_can}")


if __name__ == '__main__':
  main()