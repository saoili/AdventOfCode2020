INPUT_FILENAME = 'day1_part1.txt'
# INPUT_FILENAME = 'day1_part1_eg1.txt'


def get_nums_from_input(filename):
  all_nums = []

  with open(INPUT_FILENAME, 'r') as file:
    for line in file:
      all_nums.append(int(line))

  return all_nums


def get_ans(all_nums):
  for first in all_nums:
    for second in all_nums:
      if first == second:
        continue

      third = 2020 - first - second

      if third != second and third != first and third in all_nums:
        return first * second * third



def main():
  # print(get_ans())
  all_nums = get_nums_from_input(INPUT_FILENAME)
  # print(get_ans_theoretically_clever(all_nums))
  print(get_ans(all_nums))



if __name__ == '__main__':
  main()