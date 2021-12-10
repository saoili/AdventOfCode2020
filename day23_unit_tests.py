import day23_part2 as d


cup_game = d.CupGame(d.INPUT)
print(cup_game)
for i in range(100):
  cup_game.take_turn()  
print(cup_game)


def test_part_one_eg():
  cup_game = d.CupGame(d.INPUT_EG1)
  for i in range(100):
    cup_game.take_turn()
  assert str(cup_game) == '67384529'

def test_part_one():
  cup_game = d.CupGame(d.INPUT)
  for i in range(100):
    cup_game.take_turn()
  assert str(cup_game) == '65432978'
