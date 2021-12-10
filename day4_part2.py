# FILENAME = 'day4_part2_eg1.txt'
# FILENAME = 'day4_part1_eg2.txt'
FILENAME = 'day4_part1.txt'


VALID_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',]
VALID_YEAR_RANGES = {'byr': (1920, 2002), 'iyr': (2010, 2020), 'eyr': (2020, 2030),}
VALID_HEIGHTS = {'cm': (150, 193), 'in': (59, 76),}
VALID_HAIR_CHARS = [str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
VALID_EYE_COLOURS = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth',)


def get_passports():
  passports = []

  with open(FILENAME, 'r') as file:
    passport = ""

    for line in file:
      line = line.strip()

      if line == "":
        passports.append(passport)
        passport = ""
      else:
        passport = passport + " " + line

    passports.append(passport)

  return passports


def get_passport_detail(passport):
  fields = {}

  for line in passport.split("\n"):
    for field in line.split():
      field, value = field.split(":")
      if field in fields:
        print("welp, I wasn't expecting that")

      fields[field] = value

  return fields


def validate_year(value, year_type):
  try:
    value = int(value)
  except ValueError:
    return False

  lower, upper = VALID_YEAR_RANGES[year_type]

  return lower <= value <= upper


def validate_height(value):
  if 'cm' not in value and 'in' not in value:
    return False

  for measure in ('cm', 'in'):
    if measure in value:
      try:
        value = int(value.strip(measure))
      except ValueError:
        return False

      lower, upper = VALID_HEIGHTS[measure]

      return lower <= value <= upper


def validate_hair_colour(value):
  if value[0] != '#':
    return False

  for char in value[1:]:
    if char not in VALID_HAIR_CHARS:
      return False

  return True


def validate_pid(value):
  if len(value) != 9:
    return False

  try:
    value = int(value)
  except ValueError:
    return False

  return True


def validate_field(field, value):
  if field in ['byr', 'iyr', 'eyr',]:
    return validate_year(value, field)

  if field == 'hgt':
    return validate_height(value)

  if field == 'hcl':
    return validate_hair_colour(value)

  if field == 'ecl':
    return value in VALID_EYE_COLOURS

  if field == 'pid':
    return validate_pid(value)

  print("I didn't expect to get here")
  return False


def is_valid(passport):

  for field in VALID_FIELDS:
    if field + ':' not in passport:
      # print(f"returning false because it is missing {field}")
      return False
    # else:
    #   print(f"{field} is in it")

  fields = get_passport_detail(passport)

  for field, value in fields.items():
    if field not in VALID_FIELDS:
      continue
    
    # print(field, value, validate_field(field, value))
    if not validate_field(field, value):
      return False

  return True


def main():
  passports = get_passports()
  # print(len(passports))
  # for passport in passports:
  #   print(passport)
  #   print(is_valid(passport), "\n")

  total_valid = 0

  for passport in passports:
    if is_valid(passport):
      total_valid += 1

  print(total_valid)



if __name__ == '__main__':
  main()