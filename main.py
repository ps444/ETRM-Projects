# import "datetime" library
from datetime import datetime;

# import for access to terminal system
import sys;


# import functions I need
from price_generator_for1 import generate_random_number
from price_generator_for2 import generate_random_price

# get the first variable from command line
num = int(sys.argv[1])

# store current time in variable
start_time = datetime.now()

# run function
generate_random_number(num)

# store finished time in variable
end_time = datetime.now()




# store current time in variable
start_time_two = datetime.now()

# run functions
generate_random_price(num)

# store finished time in variable
end_time_two = datetime.now()



# calculate the difference
result_one = end_time - start_time
result_two = end_time_two - start_time_two

# calculate the difference
print(end_time - start_time)
print(end_time_two - start_time_two)



# use if statement to check which one is faster...

if result_one > result_two:
    print("Module 2 is faster")

if result_two > result_one:
    print("Module 1 is faster")