import random
import sys



num = int(sys.argv[1])


def generate_random_price(num):



    for i in range(num):

        price = round(random.uniform(0, 100), 2)
        print(f"£{price: .2f}")


generate_random_price(num)