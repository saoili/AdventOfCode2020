FILENAME = 'day18_part1_eg1.txt'
# FILENAME = 'day18_part1_eg2.txt'
FILENAME = 'day18_part1.txt'
# FILENAME = 'day18_part2_eg.txt'


def eval_no_brackets(line):
  # print(f"line in eval_no_brackets is {line}")

  if '+' not in line or '*' not in line:
    # print(f"returning eval of {line}")
    return eval(line)

  first_mul = line.find('*')
  second_mul_in_after = line[first_mul+1:].find('*')
  
  # print(f"getting eval of {line[:first_mul]} as before")
  before = eval(line[:first_mul])

  if second_mul_in_after == -1:
    # print(f"getting eval of {line[first_mul+1:]} to mul by before")
    return before * eval(line[first_mul+1:])

  second_mul = first_mul + second_mul_in_after

  # print(f"getting eval of {line[first_mul+1:second_mul+1]} as between")
  between = eval(line[first_mul+1:second_mul+1])

  # print(f"str(int(before) * int(between)) is {str(int(before) * int(between))}")
  # x = "".join(line[second_mul+1:])
  # print(f".join(line[second_mul+1:] is {x}")

  return eval_no_brackets(str(int(before) * int(between))+"".join(line[second_mul+1:]))


def evaluate_line(line):
  # print(f"evaluate_line {line}")
  if '(' not in line:
    # print(f"calling from here???")
    return eval_no_brackets(line)

  stack = []

  for i, char in enumerate(line):
    # print(f"char is {char}")
    if char != ')':
      # print("not a close, so append")
      stack.append(char)
      continue

    # print(f"got a close, trying to work from stack {stack}")
    reverse_this = []
    last = stack.pop()
    while last != '(':
      reverse_this.append(last)
      last = stack.pop()

    stack.append(str(evaluate_line("".join(reverse_this[::-1]))))

  # print(f"stack is {stack}")
  return evaluate_line("".join(stack))


def get_homework_lines():
  lines = []

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      if not line:
        continue

      lines.append(line.replace(' ', ''))

  return lines


def main():
  lines = get_homework_lines()
  # print(lines)
  total = 0

  for line in lines:
    print(f"\nline is {line}")
    ev = evaluate_line(line)
    print(f"evaulates to {ev}")
    total += ev

  print(f"\ntotal is {total}")



if __name__ == '__main__':
  main()