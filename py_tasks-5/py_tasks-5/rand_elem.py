import random

def get_random_elem(elements):
    if len(elements) > 0:
        return random.choice(elements)
    else:
        return None
