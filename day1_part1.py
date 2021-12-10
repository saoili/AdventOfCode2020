INPUT_FILENAME = 'day1_part1.txt'
# INPUT_FILENAME = 'day1_part1_eg1.txt'


def get_nums_from_input(filename):
  all_nums = []

  with open(INPUT_FILENAME, 'r') as file:
    for line in file:
      all_nums.append(int(line))

  return all_nums


def get_ans_theoretically_clever(all_nums):
  all_nums_flux = sorted(all_nums)
  all_nums.sort()

  for i in all_nums:
    next_from_end = all_nums.pop()

    while next_from_end + i < 2020:
      next_from_end = all_nums.pop()

    print(i, next_from_end, i + next_from_end)
    if i + next_from_end == 2020:
      return i * next_from_end


def get_ans_possibly_slow(all_nums):
  for num in all_nums:
    other = 2020 - num
    if other in all_nums:
      return num * other




def main():
  # print(get_ans())
  all_nums = get_nums_from_input(INPUT_FILENAME)
  # print(get_ans_theoretically_clever(all_nums))
  print(get_ans_possibly_slow(all_nums))



if __name__ == '__main__':
  main()