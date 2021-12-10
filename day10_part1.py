from collections import defaultdict


FILENAME = 'day10_part1_eg1.txt'
FILENAME = 'day10_part1_eg2.txt'
FILENAME = 'day10_part1.txt'
# FILENAME = 'day10_part2_eg.txt'


def get_joltages():
  joltages = []

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      if line:
        joltages.append(int(line))

  return sorted(joltages)


def get_differences(joltages):
  differences = defaultdict(int)

  for i, joltage in enumerate([0] + joltages[:-1]):
    next_joltage = joltages[i]
    difference = next_joltage - joltage

    # print(f"this one is {joltage}, next is {next_joltage}, difference is {difference}")

    differences[difference] += 1

  # add the last three step after the end
  differences[3] += 1

  return differences


def main():
  joltages = get_joltages()
  differences = get_differences(joltages)
  print(differences[3] * differences[1])


if __name__ == '__main__':
  main()