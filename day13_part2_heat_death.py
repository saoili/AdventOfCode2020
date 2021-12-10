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


def get_answer(bus_ids_with_t):
  i = 0

  while True:
    well_does_it = does_it_work(i, bus_ids_with_t)
    # if i % 1000000 == 0:
    #   print(i, well_does_it)
    if well_does_it:
      return i
    i += 1


def main():
  my_timestamp, bus_ids = get_timetable(FILENAME)
  # print(my_timestamp, bus_ids)
  # valid_bus_ids = [int(id) for id in bus_ids if id != 'x']
  # print(valid_bus_ids)
  # best_bus, best_wait_time = get_next_bus(my_timestamp, valid_bus_ids)
  # print(best_bus * best_wait_time)
  bus_ids_with_t = [(int(id), i) for i, id in enumerate(bus_ids) if id != 'x']
  # print(bus_ids_with_t)
  # for bus_id, i in bus_ids_with_t:
  #   print(bus_id, next_departure(1068781, bus_id))
  print(get_answer(bus_ids_with_t))

  for filename in (
    'day13_part2_eg1.txt',
    'day13_part2_eg2.txt',
    'day13_part2_eg3.txt',
    'day13_part2_eg4.txt',
    'day13_part2_eg5.txt',
    'day13_part1.txt',
  ):
    _, bus_ids = get_timetable(filename)
    bus_ids_with_t = [(int(id), i) for i, id in enumerate(bus_ids) if id != 'x']

    print(filename, get_answer(bus_ids_with_t))


if __name__ == '__main__':
  main()