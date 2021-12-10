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


def get_questions_answered_sets(group, debug=False):
  if debug:
    print(f"len(group) is {len(group)}")

  if len(group) == 1:
    if debug:
      print(f"returning len of the first person because there is only one, {group[0]}")
    return len(group[0])

  all_answers = set(group[0]).intersection(set(group[1]))

  if len(group) == 2:
    if debug:
      print(f"returning len of first two intersection because there are only two, {all_answers}")
    return len(all_answers)

  for person in group[2:]:
    all_answers = all_answers.intersection(set(person))
    if debug:
      print(f"adding on for person {person}, {all_answers}")

  if debug:
    print(f"expected to be returning the right answer, {all_answers}")
  return len(all_answers)


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
    worked = get_questions_answered(group)
    did_not_work = get_questions_answered_sets(group)
    # print(group, get_questions_answered(group), "\n\n")
    if worked != did_not_work:
      print("\n"*4)
      print(f"{group}, worked: {worked}, did_not_work: {did_not_work}")
      get_questions_answered_sets(group, True)

  print(sum((get_questions_answered(group)) for group in groups))


if __name__ == '__main__':
  main()