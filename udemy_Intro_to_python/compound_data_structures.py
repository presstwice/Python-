
# Below is an example of a compounded data structure, it's a nested dictionary
# We define pokemon and assign strings as keys, with there values being any mutable type
pokemon = {"pikachu": {"number": 5, 
                       "weight": 56.0, "type":
                       "Electric\\Normal"},
           "magikarp": {"number": 23, 
                        "weight": 0.88, 
                        "type": "dark\\ghost"}}

# Here we show how to access an pokemon in a nested dictionary
pikachu = pokemon["pikachu"]
pikachu_type = pokemon["pikachu"]["type"]

# print(pikachu_type)

# Below we show how to add a new key to the pokemon

lapras = {"number": 90, "weight": 1300.5, "type": "water"}
pokemon["lapras"] = lapras
print("pokemon = ", pokemon)

# you can also add values to existing keys like so

pokemon['pikachu']['gen_1'] = True
pokemon['magikarp']['gen_1'] = True
pokemon['lapras']['gen_1'] = True

# Then you can check the new value like so 

print(pokemon['lapras']['gen_1'])
