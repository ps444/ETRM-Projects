# My Python Learning Journey
import random;
import sys;

num = int(sys.argv[1])


def generate_random_number(parameters):
    
    for counter in range(parameters):
        print(round(random.uniform(0, 100), 2))





print( generate_random_number(num))