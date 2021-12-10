from boot_code_reader import BootCodeReader


FILENAME = 'day8_part1_eg.txt'
# FILENAME = 'day8_part1_eg2.txt'
FILENAME = 'day8_part1.txt'
# FILENAME = 'day8_part2_eg.txt'


def main():
  bcr = BootCodeReader(FILENAME)
  # bcr.debug = True

  # keep_going = True

  # while keep_going:
  #   bcr.tick()
  #   keep_going = input("keep going? > ") != 'n'

  print(bcr.accumulator_before_repeat())


if __name__ == '__main__':
  main()