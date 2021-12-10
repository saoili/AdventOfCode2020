from boot_code_reader import BootCodeReader


FILENAME = 'day8_part1_eg.txt'
# FILENAME = 'day8_part1_eg2.txt'
FILENAME = 'day8_part1.txt'
# FILENAME = 'day8_part2_eg.txt'


def get_fixed_accumulator(bcr):
  for i, (op, number) in enumerate(bcr.instructions):
    bcr.reset()
    # print(f"i is {i}, op is {op}, number is {number}")
    if op not in ('nop', 'jmp'):
      continue

    if op == 'nop':
      new_op = 'jmp'

    if op == 'jmp':
      new_op = 'nop'

    bcr.instructions[i] = (new_op, number)

    if bcr.terminates():
      return bcr.accumulator

    bcr.instructions[i] = (op, number)

  return "Well, that didn't work"
      

def main():
  bcr = BootCodeReader(FILENAME)
  # bcr.debug = True

  # keep_going = True

  # while keep_going:
  #   bcr.tick()
  #   keep_going = input("keep going? > ") != 'n'

  # print(bcr.accumulator_before_repeat())

  # print(bcr.terminates())

  print(get_fixed_accumulator(bcr))


if __name__ == '__main__':
  main()