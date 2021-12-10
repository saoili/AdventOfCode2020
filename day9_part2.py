FILENAME, PREAMBLE = 'day9_part1_eg.txt', 5
# FILENAME = 'day9_part1_eg2.txt'
FILENAME, PREAMBLE = 'day9_part1.txt', 25
# FILENAME = 'day9_part2_eg.txt'


def get_full_list():
  full_list = []

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      if line:
        full_list.append(int(line))

  return full_list


def is_valid(number, previous):
  for i, num_1 in enumerate(previous):
    for j, num_2 in enumerate(previous):
      if i == j:
        continue
      if num_1 + num_2 == number:
        return True

  return False


def get_first_wrong(full_list):
  previous = full_list[:PREAMBLE]

  for number in full_list[PREAMBLE:]:
    if not is_valid(number, previous):
      return number

    previous.pop(0)
    previous.append(number)


def get_range(full_list, sought):
  for i, first in enumerate(full_list):
    i_in_full = i + 1
    current_list = [first]

    # print(f"first is {first}, i in full is {i_in_full}")
    for j, last in enumerate(full_list[i_in_full:]):
      j_in_full = j + i_in_full + 1

      current_list.append(last)

      sum_current = sum(current_list)

      if sum_current == sought:
        return min(current_list), max(current_list)

      if sum_current > sought:
        continue      

  return 0, 0 


def main():
  full_list = get_full_list()
  first_wrong = get_first_wrong(full_list)
  smallest, largest = get_range(full_list, first_wrong)
  print(f"smallest is {smallest}, largest is {largest}")
  print(smallest + largest)


if __name__ == '__main__':
  main()