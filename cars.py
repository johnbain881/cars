makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"),
)

models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6)
)

colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

available_car_colors = (
  (1, 1), (1, 2), (1, 7),
  (2, 1), (2, 3), (2, 7),
  (3, 2), (3, 3), (3, 7),
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8),
  (6, 2), (6, 6), (6, 7),
  (7, 1), (7, 3), (7, 7),
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7),
  (10, 2), (10, 5), (10, 7),
  (11, 3), (11, 6), (11, 8),
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8),
  (14, 2), (14, 5), (14, 8),
  (15, 1), (15, 4), (15, 7)
)


# car_dict = {}

# for make in makes:
#   car_dict[make[1]] = {}
#   for model in models:
#     if make[0] == model[2]:
#       car_dict[make[1]][model[1]] = []
#       for color in available_car_colors:
#         if model[0] == color[0]:
#           # print(f"model: {model} color: {color[0]}")
#           car_dict[make[1]][model[1]].append(colors[color[1]-1][1])

new_car_dict = {}
new_car_dict = {make[1]: {model[1]: [colors[color[1]-1][1] for color in available_car_colors if model[0] == color[0] ] for model in models if make[0] == model[2]} for (make) in makes}
print("".join(list({f"\n--------\n\n{car}\n\n--------\n" + "".join(f"\n{make} is available in" + "".join(f" {color}" for color in model) for (make, model) in makes.items()) for (car, makes) in new_car_dict.items()})))
# print(new_car_dict)

# for car, makes in new_car_dict.items():
#   print(f"--------\n\n{car}\n\n--------\n")
#   for make, model in makes.items():
#     color_string = ""
#     for color in model:
#       color_string = color_string + ', ' + color
#     color_string = color_string.replace(", ", "", 1)
#     print(f"{make} is available in {color_string}")

