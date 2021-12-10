from collections import defaultdict

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

# FILENAME = 'day2_part1_eg1.txt'
FILENAME = 'day2_part1.txt'


def password_map_from_file():
  password_map = defaultdict(list)
  i = 0

  with open(FILENAME, 'r') as file:
    for line in file:
      # print(f"parsing line {line}")
      rules, password = line.strip().split(':')
      times, letter = rules.split(' ')
      lower, upper = times.split('-')
      lower = int(lower)
      upper = int(upper)
      password_map[(letter, lower, upper)].append(password)
      # print(i)
      i += 1

  return password_map


def ans(password_map):
  valid = 0

  for (letter, lower, upper), passwords in password_map.items():
    for password in passwords:
      count = password.count(letter)
      if count >= lower and count <= upper:
        # print(f"{valid}: saying that   valid for    {letter, lower, upper}    {password}, count was {count}")
        valid += 1
      # else:
      #   print(f"{valid}: saying that not valid for  {letter, lower, upper}    {password}, count was {count}")

  return valid


def main():
  password_map = password_map_from_file()
  print(password_map)
  print(len(password_map))
  print(ans(password_map))

if __name__ == '__main__':
  main()


