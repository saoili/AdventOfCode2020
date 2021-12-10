FILENAME = 'day13_part1_eg1.txt'
# FILENAME = 'day13_part1_eg2.txt'
FILENAME = 'day13_part1.txt'
# FILENAME = 'day13_part2_eg.txt'


def get_timetable():
  my_timestamp = None

  with open(FILENAME, 'r') as file:
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


def main():
  my_timestamp, bus_ids = get_timetable()
  # print(my_timestamp, bus_ids)
  valid_bus_ids = [int(id) for id in bus_ids if id != 'x']
  # print(valid_bus_ids)
  best_bus, best_wait_time = get_next_bus(my_timestamp, valid_bus_ids)
  print(best_bus * best_wait_time)



if __name__ == '__main__':
  main()