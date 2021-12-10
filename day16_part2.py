from collections import defaultdict

FILENAME = 'day16_part1_eg1.txt'
# FILENAME = 'day16_part1_eg2.txt'
FILENAME = 'day16_part1.txt'
# FILENAME = 'day16_part2_eg1.txt'


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


def is_valid_ticket(ticket, rules):
  for number in ticket:
    if not is_valid_for_something(number, rules):
      return False

  return True


def get_valid_tickets(tickets, rules):
  valid_tickets = []

  for ticket in tickets:
    if is_valid_ticket(ticket, rules):
      valid_tickets.append(ticket)

  return valid_tickets


def is_valid_for_something(number, rules):
  for rule_name, rule_ranges in rules.items():
    if is_valid_for_rule(number, rule_ranges):
      return True

  return False


def is_valid_for_rule(number, rule_ranges):
  for rule_range in rule_ranges:
    lower, upper = rule_range
    if lower <= number <= upper:
      return True

  return False


def valid_for_all(tickets, rule_ranges, position):
  for i, ticket in enumerate(tickets):
    if not is_valid_for_rule(ticket[position], rule_ranges):
      # print(f"{ticket[position]} for ticket {i} is not valid for position {position}", end=" ")
      return False

  return True


def get_fields(tickets, rules):
  options = defaultdict(set)

  for rule_name, rule_ranges in rules.items():
    # print(f"for rule name {rule_name}")
    for position in range(len(tickets[0])):
      # print(f"for position {position}", end=" ")
      if valid_for_all(tickets, rule_ranges, position):
        # print(f"is valid for rule_ranges {rule_ranges}")
        options[position].add(rule_name)
      # else:
      #   print(f"is not valid for rule_ranges {rule_ranges}")

  return options


def whittle_options(options):
  new_options = options.copy()

  for position, options_for in options.items():
    if len(options_for) == 1:
      option = list(options_for)[0]
      for position_new, options_for_new in new_options.items():
        if position == position_new:
          continue
        options_for_new.discard(option)

  return new_options, new_options == options


def fully_whittled(options):
  for position, options_for in options.items():
    if len(options_for) > 1:
      return False

  return True


def main():
  rules, my_ticket, tickets = get_notes()
  valid_tickets = get_valid_tickets(tickets, rules)
  # print(valid_tickets)
  options = get_fields(valid_tickets, rules)
  # print(f"options is {options}")
  options, whittled = whittle_options(options)
  # print(f"options is {options}")
  print(whittled)
  print(f"fully whittled?: {fully_whittled(options)}")
  options, whittled = whittle_options(options)
  # print(f"options is {options}")
  print(whittled)
  print(f"fully whittled?: {fully_whittled(options)}")
  
  while not fully_whittled(options):
    options, whittled = whittle_options(options)
    if not whittled:
      print("boo")
      break

  print(fully_whittled(options))
  print(f"options is {options}")

  ans = 1

  for position, options_for in options.items():
    option = list(options_for)[0]
    if 'departure' in option:
      print(option)
      ans *= my_ticket[position]

  print(f"hopefully the answer is {ans}")




if __name__ == '__main__':
  main()