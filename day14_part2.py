FILENAME = 'day14_part1_eg1.txt'
# FILENAME = 'day14_part1_eg2.txt'
FILENAME = 'day14_part1.txt'
# FILENAME = 'day14_part2_eg1.txt'


def get_program():
  program = []
  mask = None

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      if not line:
        continue

      if 'mask' in line:
        if mask is not None:
          program.append({mask: instructions})
        mask = line.replace('mask = ', '')
        instructions = []
      else:
        line = line.replace('mem[', '')
        mem, num = [int(i) for i in line.split('] = ')]
        instructions.append((mem, num))

    program.append({mask: instructions})

  return program


def apply_mask(mask, num):
  binary = bin(num)[:1:-1]
  rev_mask = mask[::-1]
  # print(rev_mask)

  len_binary = len(binary)

  answer = 0

  for i, mask_i in enumerate(rev_mask):
    if mask_i == '1':
      # print(f"mask at {i} is 1")
      this_one = True
    elif mask_i == '0':
      # print(f"mask at {i} is 0")
      this_one = False
    else:
      # print(f"mask at {i} is {mask_i}")
      if i < len_binary:
        # print(f"binary at {i} is {binary[i]}")
        this_one = binary[i] == '1'
      else:
        this_one = False
    if this_one:
      # print(f"this one is true so adding {2 ** i}")
      answer += 2 ** i

  return answer


def parse_answerish(answerish):
  print(f"answerish is {answerish}")
  answers = [0]

  for i, place in enumerate(answerish):
    if place in ['x', 1]:
      new_answers = []
      for answer in answers:
        new_answers.append(answer + 2**i)
      if place == 'x':
        answers += new_answers
      else:
        answers = new_answers

  return answers


def apply_mask_to_mem(mask, mem):
  binary = bin(mem)[:1:-1]
  rev_mask = mask[::-1]

  len_binary = len(binary)

  answerish = []

  for i, mask_i in enumerate(rev_mask):
    if mask_i == '0':
      # print(f"mask at {i} is 1")
      if i < len_binary:
        answerish.append(int(binary[i]))
      else:
        answerish.append(0)
    elif mask_i == '1':
      # print(f"mask at {i} is 0")
      answerish.append(1)
    else:
      answerish.append('x')

  return parse_answerish(answerish)


def run_program(program):
  output = {}

  for sub_program in program:
    # print(f"sub_program is {sub_program}")
    # print(f"sub_program.items() is {list(sub_program.items())}")

    for mask, instructions in sub_program.items():
      print("\n")
      for instruction in instructions:
        # print(f"instruction is {instruction}")
        mem, num = instruction
        # after = apply_mask(mask, num)
        after = num
        # print(f"mask is length {len(mask)} and num in bin is len {len(bin(num))}")
        # if len(bin(num)) >= len(mask):
        #   print(f"apply {mask} to {num} and then put in {mem}")
        #   print(f"mask is length {len(mask)} and num in bin is len {len(bin(num))}")
        new_mems = apply_mask_to_mem(mask, mem)
        print(f"apply {mask} to {num} and then put in each of {new_mems}")
        for new_mem in new_mems:     
          output[new_mem] = after

  print(f"output is {output}")

  return sum(output.values())


def main():
  program = get_program()
  # print(program)
  print(run_program(program))


if __name__ == '__main__':
  main()