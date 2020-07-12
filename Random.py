import random

random_exp = [IndexError, SyntaxError, KeyboardInterrupt]

def random_exception(sarasas):
    return random.choice(sarasas)

for i in range(6):
    x = random_exception(random_exp)
    print(x)
