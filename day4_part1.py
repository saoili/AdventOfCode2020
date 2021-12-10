# FILENAME = 'day4_part1_eg1.txt'
# FILENAME = 'day4_part1_eg2.txt'
FILENAME = 'day4_part1.txt'


def get_passports():
  passports = []

  with open(FILENAME, 'r') as file:
    # passport = []
    passport = ""

    for line in file:
      line = line.strip()

      if line == "":
        passports.append(passport)
        # passport = []
        passport = ""
      else:
        # passport += line.split()
        passport = passport + line

    passports.append(passport)

  return passports


def is_valid(passport):

  for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
    if field + ':' not in passport:
      # print(f"returning false because it is missing {field}")
      return False
    # else:
    #   print(f"{field} is in it")

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