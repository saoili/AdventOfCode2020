from math import gcd
from functools import reduce


def chinese_remainder(n, a):
    print("in chinese_remainder")
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

FILENAME = 'day13_part1_eg1.txt'
# FILENAME = 'day13_part1_eg2.txt'
# FILENAME = 'day13_part1.txt'
# FILENAME = 'day13_part2_eg.txt'


def get_timetable(filename):
  my_timestamp = None

  with open(filename, 'r') as file:
    for line in file:
      line = line.strip()
      if not line:
        continue

      if my_timestamp is None:
        my_timestamp = int(line)
      else:
        bus_ids = line.split(',')

  return my_timestamp, bus_ids


def get_next_bus(my_timestamp, valid_bus_ids):
  best_bus = None

  for bus in valid_bus_ids:
    wait_time = bus - (my_timestamp % bus)
    # print(f"next_arrival time for {bus} is {wait_time}")

    if best_bus is None or best_wait_time > wait_time:
      best_wait_time = wait_time
      best_bus = bus

  return best_bus, best_wait_time


def next_departure(t, bus):
  # print(t, bus, t % bus)
  return (bus - (t % bus)) % bus


def does_it_work(timestamp, bus_ids_with_t):
  for bus_id, t in bus_ids_with_t:
    if next_departure(timestamp, bus_id) != t:
      return False

  return True


def all_pairwise_coprime(numbers):
  for i, first in enumerate(numbers):
    for second in numbers[i+1:]:
      if gcd(first, second) > 1:
        print(f"gcd of {first} and {second} is {gcd(first, second)}\n\n\n")
        return False

  return True


def get_things_t_equals(bus_ids_with_t):
  things = []

  for bus, req_sec in bus_ids_with_t:
    thing = bus - req_sec
    while thing <= 0:
      # print(f"in while for thing {thing}, bus {bus} and req_sec {req_sec}")
      thing += bus
    # print(f"bus is {bus}, req_sec is {req_sec}, thing is {thing}")
    things.append((thing, bus))

  return things


def get_s(capital_n, n):
  a = capital_n
  b = n

  gcd, x, y = get_egcd(a, b)

  return x


def get_egcd(a, b):
  if a == 0:
    return b, 0, 1

  gcd, x, y = get_egcd(b % a, a)
  return gcd, y - (b//a) * x, x


def get_s_old(capital_n, n):
  # Using the   Extended Euclidean algorithm, we can find integers r and s
  # such that r*n + s*capital_n/n = 1
  # ax + by = gcd(a, b)
  # but a and b are co-prime, so gcd(a, b) is 1
  # so ax + by = 1

  # b here is capital_n/n (so the multilpication of all other busses)

  a = n
  b = capital_n/n
  print(f"a is {a}")
  print(f"b is {b}")

  # so now we're looking for what the algorithm calls y
  # y is the modular multiplicative inverse of b modulo a
  # In mathematics, particularly in the area of number theory,
  # a modular multiplicative inverse of an integer a
  # is an integer x such that the product ax is congruent to 1
  # with respect to the modulus m.[1] 

  # a modular multiplicative inverse of an integer a
  # is an integer y such that the product 'by' is congruent to 1
  # with respect to the modulus a.[1] 

  y = 1

  while True:
    if b * y % a == 1:
      return y
    y += 1



def get_answer_old(bus_ids_with_t):
  # Chinese Remainder Theorem

  # things is [(thing, bus)...]
  # where thing is the thing that is t is equal to
  # modulo that bus
  things = get_things_t_equals(bus_ids_with_t)
  print(f"things is {things}")

  capital_n = 1
  for a, n in things:
    capital_n *= n

  print(f"N is {capital_n}")
  answer = 0
  for a, n in things:
    s = get_s(capital_n, n)
    print(f"for a {a} and n {n}, s is {s}")
    answer += a * s * capital_n / n

  return answer % capital_n


def get_answer(bus_ids_with_t):
  things = get_things_t_equals(bus_ids_with_t)

  n = [i[1] for i in things]
  a = [i[0] for i in things]

  return chinese_remainder(n, a)


def satisfies(bus, wait_time, answer):
  time_to_first_time_after_answer = bus - (answer % bus)
  # print(f"time_to_first_time_after_answer is {time_to_first_time_after_answer}")

  if wait_time == time_to_first_time_after_answer:
    return True

  if wait_time == 0:
    return True

  # print(f"time_to_first_time_after_answer % {wait_time} is {time_to_first_time_after_answer % wait_time}")

  return wait_time % bus == time_to_first_time_after_answer


def main():
  my_timestamp, bus_ids_strings = get_timetable(FILENAME)
  # print(my_timestamp, bus_ids_strings)
  # valid_bus_ids = [int(id) for id in bus_ids_strings if id != 'x']
  # print(valid_bus_ids)
  # best_bus, best_wait_time = get_next_bus(my_timestamp, valid_bus_ids)
  # print(best_bus * best_wait_time)
  bus_ids_with_t = [(int(id), i) for i, id in enumerate(bus_ids_strings) if id != 'x']
  # print(bus_ids_with_t)
  # for bus_id, i in bus_ids_with_t:
  #   print(bus_id, next_departure(1068781, bus_id))
  # print(get_answer(bus_ids_with_t))

  for filename in (
    'day13_part1_eg1.txt',
    'day13_part1_eg1.txt',
    'day13_part2_eg1.txt',
    'day13_part2_eg2.txt',
    'day13_part2_eg3.txt',
    'day13_part2_eg4.txt',
    'day13_part2_eg5.txt',
    'day13_part2_eg6.txt',
    'day13_part2_eg7.txt',
    'day13_part1.txt',
  ):
    print("\n")
    print(filename)
    _, bus_ids_strings = get_timetable(filename)
    bus_ids_with_t = [(int(id), i) for i, id in enumerate(bus_ids_strings) if id != 'x']
    bus_ids_with_t.sort(key=lambda b: b[0], reverse=True)
    # print(bus_ids_with_t)
    bus_ids = [b[0] for b in bus_ids_with_t]
    # wait_times = [b[1] for b in bus_ids_with_t]

    # print(wait_times)
    if not all_pairwise_coprime(bus_ids):
      print("well then you have a whole other problem")
    # print(all_pairwise_coprime(wait_times))
    # things_t_equals = get_things_t_equals(bus_ids_with_t)
    # print(things_t_equals)
    # print(all_pairwise_coprime([t[0] for t in things_t_equals]))
    answer = get_answer(bus_ids_with_t)
    ao = get_answer_old(bus_ids_with_t)
    print(filename, answer)
    print(filename, ao)

    for bus, t in bus_ids_with_t:
      s = satisfies(bus, t, answer)
      print(f"bus is {bus}, wait time is {t}, satisfies is {s} for {answer}")
      s = satisfies(bus, t, ao)
      print(f"bus is {bus}, wait time is {t}, satisfies is {s} for {ao}")
      
      

  # print(get_egcd(30, 50))
  n = [3, 5, 7]
  a = [2, 3, 2]
  # print(chinese_remainder(n, a))


if __name__ == '__main__':
  main()