# from random import choice
# print(choice("Head", "Tails"))

import random
print(random.choice(["heads", "tails"]))
print(random.randint(0, 10))

cards=["Unnati", "Bimal", "Gupta"]
random.shuffle(cards)
print(cards)