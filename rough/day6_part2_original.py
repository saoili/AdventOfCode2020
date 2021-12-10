FILENAME = 'day6_part1_eg1.txt'
# FILENAME = 'day6_part1_eg2.txt'
FILENAME = 'day6_part1.txt'


def get_groups():
  groups = []

  with open(FILENAME, 'r') as file:
    group = []
    for line in file:
      line = line.strip()
      if line == '':
        groups.append(group)
        group = []
      else:
        group.append(line)      

  groups.append(group)
  return groups


def get_questions_answered(group):
  all_answers = set(group[0])

  for person in group:
    for answer in all_answers.copy():
      if answer not in person:
        all_answers.remove(answer)

  return len(all_answers)


def main():
  groups = get_groups()
  for group in groups:
    print(group, get_questions_answered(group), "\n\n")

  print(sum((get_questions_answered(group)) for group in groups))


if __name__ == '__main__':
  main()