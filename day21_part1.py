from collections import defaultdict


FILENAME = 'day21_part1_eg1.txt'
FILENAME = 'day21_part1.txt'

# FILENAME = 'day21_part1_eg2.txt'
# FILENAME = 'day21_part2.txt'
# FILENAME = 'day21_part2_eg1.txt'
# FILENAME = 'day21_part2_eg2.txt'


def get_allergens():
  all_allergens = []

  with open(FILENAME, 'r') as file:
    for line in file:
      line = line.strip()
      
      if not line:
        continue

      ingredients, allergens = line.split('(contains ')
      ingredients = ingredients.split()
      allergens = allergens.replace(')','').replace(',','').split()

      all_allergens.append((ingredients, allergens))

  return all_allergens


def get_ingredient_for_allergens(all_allergens):
  # print(f"in get with allergens {all_allergens[0]}")
  x = {}

  for ingredients, allergens in all_allergens:
    # print(f"ingredients is {ingredients}")
    # print(f"allergens is {allergens}")
    for allergen in allergens:
      current_ingredients = set(ingredients)
      previous_possible_ingredients = x.get(allergen)
      if previous_possible_ingredients is None:
        possible_ingredients = current_ingredients
      else:
        possible_ingredients = previous_possible_ingredients.intersection(current_ingredients)

      x[allergen] = possible_ingredients

  ready_to_return = True
  most_allergens = []
  remove_ingredients = []
  remove_allergens = []

  # print(f"x is {x}")

  for allergen, ingredients in x.items():
    # print(f"ingredients is {ingredients} allergen is {allergen}")
    if len(ingredients) == 1:
      remove_ingredients.append(list(ingredients)[0])
      remove_allergens.append(allergen)
    else:
      ready_to_return = False

  if ready_to_return:
    return x

  # print(f"remove_ingredients is {remove_ingredients}")
  # print(f"remove_allergens is {remove_allergens}")

  for ingredients, allergens in all_allergens:
    new_allergens = []

    for allergen in allergens:
      if allergen not in remove_allergens:
        new_allergens.append(allergen)

    if new_allergens:
      new_ingredients = []
      for ingredient in ingredients:
        if ingredient not in remove_ingredients:
          new_ingredients.append(ingredient)
      most_allergens.append((new_ingredients, new_allergens))
    #   print(f"\ningredients is {ingredients}")
    #   print(f"new_ingredients is {new_ingredients}")
    #   print(f"allergens is {allergens}")
    #   print(f"new_allergens is {new_allergens}")
    # else:
    #   print(f"no new allergens")

  # print(f"most_allergens is {most_allergens}")
  sub_x = get_ingredient_for_allergens(most_allergens)

  x.update(sub_x)

  return x


def get_cannot_contain_allergen(all_allergens):
  allergen_to_ingredient_set = get_ingredient_for_allergens(all_allergens)
  ingredient_to_allergen = {list(i)[0]: a for a, i in allergen_to_ingredient_set.items()}

  ingredient_appearances = 0

  for ingredients, allergens in all_allergens:
    for ingredient in ingredients:
      if ingredient not in ingredient_to_allergen:
        ingredient_appearances += 1

  return ingredient_appearances


def main():
  all_allergens = get_allergens()
  print(get_cannot_contain_allergen(all_allergens))


if __name__ == '__main__':
  main()