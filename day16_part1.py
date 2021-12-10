from collections import defaultdict

FILENAME = 'day16_part1_eg1.txt'
# FILENAME = 'day16_part1_eg2.txt'
FILENAME = 'day16_part1.txt'
# FILENAME = 'day16_part2_eg.txt'


def split_ticket(ticket):
  return [int(t) for t in ticket.split(',')]


def get_notes():
  rules = {}
  tickets = []

  with open(FILENAME, 'r') as file:
    rules_raw, my_ticket, tickets_raw = file.read().split("\n\n")

  for rule in rules_raw.split("\n"):
    rule_name, rule_ranges = rule.split(": ")
    x = []
    for rule_range in rule_ranges.split(" or "):
      lower, upper = rule_range.split('-')
      lower = int(lower)
      upper = int(upper)
      x.append((lower, upper))
    rules[rule_name] = x

  my_ticket = split_ticket(my_ticket.split("\n")[-1])

  # skip the 'nearby tickets' row
  for ticket in tickets_raw.split("\n")[1:]:
    tickets.append(split_ticket(ticket))

  return rules, my_ticket, tickets


def is_valid_for_something(number, rules):
  for rule_name, rule_ranges in rules.items():
    for rule_range in rule_ranges:
      lower, upper = rule_range
      if lower <= number <= upper:
        return True
  return False


def scanning_validity(rules, tickets):
  invalid_numbers = 0

  for ticket in tickets:
    for number in ticket:
      if not is_valid_for_something(number, rules):
        print(f"{number} isn't valid for anything")
        invalid_numbers += number

  return invalid_numbers


def main():
  rules, my_ticket, tickets = get_notes()
  print(scanning_validity(rules, tickets))




if __name__ == '__main__':
  main()