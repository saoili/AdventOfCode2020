import re
import sys
from collections import defaultdict


FILENAME = 'day19_part1_eg1.txt'
# FILENAME = 'day19_part1_eg2.txt'
FILENAME = 'day19_part1.txt'
# FILENAME = 'day19_part2_eg1.txt'


class Rule():
  def __init__(self, name, raw, rules, rules_raw):
    rules[name] = self
    # print(f"in init for {name} with raw {raw}")
    self.name = name
    raw = raw.replace('"', '')

    self.all = []

    all_letters = True

    for bit in raw.split():
      # print(f"  bit is {bit}")
      if bit in ['a', 'b']:
        self.all.append(bit)
      elif bit.isnumeric():
        rule = rules.get(bit)
        if rule is None:
          # print(f"{bit} apparetly wasn't in there")
          rule = Rule(bit, rules_raw.get(bit), rules, rules_raw)
        # else:
        #   print("should get here sometimes")
        self.all.append(rule)
        all_letters = False
      else:
        if bit != '|':
          print(f"dang, bit was '{bit}'")
          sys.exit()
        all_letters = False
        self.all.append(bit)

    if all_letters:
      self.fully_processed = True
      self._text = "".join(raw)
    else:
      self.fully_processed = False
      self.process()


  def process(self):
    if self.fully_processed:
      return

    # print(f"processing for {self.name} with self.all {self.all}")
    before = ""
    after = ""
    have_hit_or = False
 
    for thing in self.all:
      if thing == '|':
        have_hit_or = True
        continue
      if not have_hit_or:
        before = before + thing.text
      else:
        after = after + thing.text

    if have_hit_or:
      self._text = f"({before}|{after})"
    else:
      self._text = before

    self.fully_processed = True

  @property
  def text(self):
    self.process()
    return self._text


def get_rules(raw):
  rules = {}
  for rule in raw.split("\n"):
    name, details = rule.split(': ')
    rules[name] = details

  return rules


def get_rules_and_messages():
  with open(FILENAME, 'r') as file:
    rules_raw, messages_raw = file.read().split("\n\n")

  return get_rules(rules_raw), messages_raw.split("\n")


def main():
  rules, messages = get_rules_and_messages()
  # print(f"rules is {rules}")
  # for name, rule in rules.items():
  #   if 'a' in rule or 'b' in rule:
  #     print(name, rule)
  #   if rule.count('|') > 1:
  #     print(f"{name} has more than one or, it is {rule}")

  rules_dict = {}

  for name, rule in rules.items():
    if rules_dict.get(name) is None:
      rule_obj = Rule(name, rule, rules_dict, rules)
    # print(f"rules_dict.get({name}) is {rules_dict.get(name)}")

  # print("\n")

  for name in sorted(list(rules_dict.keys())):
    rule = rules_dict.get(name)
    # print(f"rule is {rule.name}")
    # print(f"text is {rule.text}\n")
    # print(f"{rule.name}: {rule.text}")

  # print(rules_dict)

  messages_that_match = 0
  re_0 = rules_dict['0'].text
  print(f"re_0 is {re_0}")

  for message in messages:
    if re.fullmatch(re_0, message):
      # print(f"{message} matches")
      messages_that_match += 1
    # else:
    #   print(f"{message} doesn't match")

  print(f"a total of {messages_that_match} match")




if __name__ == '__main__':
  main()