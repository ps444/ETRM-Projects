# import "datetime" library
from datetime import datetime;

# import for access to terminal system
import sys;


# import functions I need
from price_generator_for1 import generate_random_number
from price_generator_for2 import generate_random_price_numpy

# get the first variable from command line
num = int(sys.argv[1])

def time_function(func, parameter):
    # store current time in variable
    start_time = datetime.now()

    # run function
    func(parameter)

    # store finished time in variable
    end_time = datetime.now()

    # calculate the time it took
    result = end_time - start_time

    return { 
        'start_time': start_time, 
        'end_time': end_time, 
        'result': result 
    } 
  
first_example = time_function(generate_random_number, num)
second_example = time_function(generate_random_price_numpy, num)


print(first_example['result'])
print(second_example['result'])

# use if statement to check which one is faster...
if first_example['result'] > second_example['result']:
    print("Second Example is faster")

if second_example['result'] > first_example['result']:
    print("First Example is faster")