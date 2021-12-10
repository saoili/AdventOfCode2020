FILENAME = 'day18_part1_eg1.txt'
# FILENAME = 'day18_part1_eg2.txt'
FILENAME = 'day18_part1.txt'
# FILENAME = 'day18_part2_eg.txt'


def eval_no_brackets(line):
  # print(f"line in eval_no_brackets is {line}")
  first_op = None
  second_op = None
  first_digits = []
  second_digits = []
  after = []

  for char in line:
    if second_op is not None:
      after.append(char)
      continue
    if char in ['+', '*']:
      if first_op is None:
        first_op = char
      else:
        second_op = char
    else:
      if first_op is None:
        first_digits.append(char)
      else:
        second_digits.append(char)

  # print(f"first_op is {first_op}, second_op is {second_op}", end=" ")
  # print(f"first_digits is {first_digits}, second_digits is {second_digits}", end=" ")
  # print(f"after is {after}")

  first_number = int("".join(first_digits)) 

  if first_op is None:
    return first_number

  second_number = int("".join(second_digits))

  if first_op is '+':
    number = first_number + second_number
  else:
    number = first_number * second_number

  if second_op is None:
    return number

  return eval_no_brackets(str(number) + second_op + "".join(after))



  # first_plus = line.find('+')
  # first_mul = line.find('*')
  # count_plus = line.count('+')
  # count_mul = line.count('*')

  # if count_plus == 0:
  #   if count_mul == 0:
  #     return int(line)
  #   if count_mul == 1:
  #     return int(line[:first_mul] * line[first_mul+1:])
  #   # no plusses, more than one mul



  # # print(f"line is {line}")
  # # print(f"first_plus is {first_plus}")
  # # print(f"first_mul is {first_mul}")
  # # print(f"line[:first_mul] is {line[:first_mul]}")
  # # print(f"line[first_mul+1:] is {line[first_mul+1:]}")
  # # print(f"line[:first_plus] is {line[:first_plus]}")
  # # print(f"line[first_plus+1:] is {line[first_plus+1:]}")


  # if first_plus == -1 and first_mul == -1:
  #   print("returning int line")
  #   return int(line)

  # print(f"first_plus is {first_plus} and first_mul is {first_mul}")

  # if first_plus == -1 or (first_mul >=0 and first_mul < first_plus):
  #   first_op = '*'
  #   first_op_i = first_mul
  # else:
  #   first_op = '+'
  #   first_op_i = first_plus

  # # print(f"first_op is {first_op} at {first_op_i}")
  # # print(f"before is int of {line[:first_op_i]}")
  # # print(f"after is eval of {line[first_op_i+1:]}")

  # before = int(line[:first_op_i])
  # after = eval_no_brackets(line[first_op_i+1:])

  # # print(f"before is {before}")
  # # print(f"after is {after}")


  # if first_op == '*':
  #   return before * after
  # else:
  #   return before + after


  # if first_plus == -1:
  #   if first_mul == -1:
  #     return int(line)
  #   return int(line[:first_mul]) * eval_no_brackets(line[first_mul+1:])
  # if first_mul < first_plus:
  #   return int(line[:first_mul]) * eval_no_brackets(line[first_mul+1:])
  # return int(line[:first_plus]) + eval_no_brackets(line[first_plus+1:])



def evaluate_line(line):
  print(f"evaluate_line {line}")
  if '(' not in line:
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

    print("Huh, I think I never get here")
    print("no, I did, so what didn't that fail? Mysteries of the universe")
    stack.append(str(evaluate_line(reverse_this[::-1])))

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