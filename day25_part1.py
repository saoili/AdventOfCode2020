FILENAME = 'day25_part1_eg1.txt'
FILENAME = 'day25_part1.txt'

SUBJECT_NUMBER = 7
MOD_BY = 20201227


def get_keys():
  key_one = None

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      
      if not line:
        continue

      if key_one is None:
        key_one = int(line)

      else:
        key_two = int(line)

  return key_one, key_two


def find_loop_size(key):
  value = 1
  loop_size = 0

  while True:
    loop_size += 1
    value *= SUBJECT_NUMBER
    value = value % MOD_BY
    if value == key:
      return loop_size


def transform(loop_size, subject_number):
  value = 1

  for i in range(loop_size):
    value *= subject_number
    value = value % MOD_BY

  return value


def main():
  card_key, door_key = get_keys()
  card_loop_size = find_loop_size(card_key)
  door_loop_size = find_loop_size(door_key)
  print(transform(card_loop_size, door_key))
  print(transform(door_loop_size, card_key))
  


  

if __name__ == '__main__':
  main()