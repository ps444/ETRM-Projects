import random



def generate_random_number(parameters):

    prices = []

    for counter in range(parameters):
        prices.append(round(random.uniform(0, 100), 2))

    return prices

