# FILENAME = 'day5_part1_eg.txt'
# FILENAME = 'day5_part1_eg2.txt'
FILENAME = 'day5_part1.txt'



def get_boarding_passes():
  boarding_passes = []

  with open(FILENAME, 'r') as file:
    for line in file:
      boarding_passes.append(line.strip())

  return boarding_passes


def get_row(row_str):
  lower = 0
  upper = 127
  thingie = 64

  for letter in row_str:
    if letter == 'F':
      upper -= thingie
    else:
      lower += thingie
    thingie /= 2

  return int(lower)


def get_number(number_str):
  lower = 0
  upper = 7
  thingie = 4

  for letter in number_str:
    if letter == 'L':
      upper -= thingie
    else:
      lower += thingie
    thingie /= 2

  return int(lower)  


def get_seat_id(boarding_pass):
  row = get_row(boarding_pass[:7])
  number = get_number(boarding_pass[7:])
  return row * 8 + number


def main():
  boarding_passes = get_boarding_passes()
  for boarding_pass in boarding_passes:
    print(boarding_pass, get_seat_id(boarding_pass))
  print(max([get_seat_id(b) for b in boarding_passes]))


if __name__ == '__main__':
  main()