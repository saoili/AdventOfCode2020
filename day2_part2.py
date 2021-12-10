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
      first, second = times.split('-')
      first_index = int(first) - 1
      second_index = int(second) - 1
      password_map[(letter, first_index, second_index)].append(password.strip())
      # print(i)
      i += 1

  return password_map


def ans(password_map):
  valid = 0

  for (letter, fi, si), passwords in password_map.items():
    for p in passwords:
      if p[fi] == letter and p[si] != letter or p[fi] != letter and p[si] == letter:
        valid += 1
        print(f"{valid}: saying that   valid for    {letter, fi, si, p}    first is {p[fi]} second is {p[si]}")
      else:
        print(f"{valid}: saying that not valid for  {letter, fi, si, p}    first is {p[fi]} second is {p[si]}")

  return valid


def main():
  password_map = password_map_from_file()
  # print(password_map)
  print(len(password_map))
  print(ans(password_map))

if __name__ == '__main__':
  main()


