import random
import sys


num = int(sys.argv[1])

def generate_random_number(parameters):

    prices = []

    for counter in range(parameters):
        prices.append(round(random.uniform(0, 100), 2))

    return prices

