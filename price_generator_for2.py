

import numpy as np

def generate_random_price_numpy(num_prices):

    """
    generate an array of random prices using NumPy
    Returns a list prices rounded to 2 decimal places
    """
    
    prices = np.random.uniform(0,100,num_prices) #Generate all in one cal
    rounded_prices = np.round(prices, 2) #Round prices to 2 decimals
    
    return rounded_prices.tolist() #Convert NumPy array to Python list

