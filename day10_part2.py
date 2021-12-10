from collections import defaultdict


FILENAME = 'day10_part1_eg1.txt'
FILENAME = 'day10_part1_eg2.txt'
FILENAME = 'day10_part1.txt'
# FILENAME = 'day10_part1_eg3.txt'
# FILENAME = 'day10_part2_eg.txt'


def get_joltages():
  joltages = []

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      if line:
        joltages.append(int(line))

  return sorted(joltages)


def get_answer(current_list, answers_so_far={}):
  if len(current_list) == 1:
    return 1
  answer = 0
  first = current_list.pop(0)

  answer_we_already_have = answers_so_far.get(first)
  if answer_we_already_have:
    return answer_we_already_have

  for i in range(3):
    if i == len(current_list):
      break
    next_joltage = current_list[i]
    if next_joltage - first > 3:
      break

    answer += get_answer(current_list[i:])

  answers_so_far[first] = answer
  return answer


def main():
  joltages = get_joltages()
  print(get_answer([0] + joltages))


if __name__ == '__main__':
  main()