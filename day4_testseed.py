import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
chance = ["Heads", "Tails"]
flip = random.randint(0, 1)

print(chance[flip])