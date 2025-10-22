# My Python Learning Journey: Random Price Generator

Overview
This project contains Python scripts demonstrating two methods to generate random prices:

    Using Python's built-in random library with a simple loop.

    Using the optimized NumPy library for fast random number generation.

The goal is to compare their performance and understand the differences. This is the perfect starting point because:

    It teaches about performance measurement.
    It introduces different Python Libraries
    It helps to build good habits around benchmarking.

Requirements
    Python 3.12.2 installed

    NumPy library (only for the NumPy-based generator)

Install NumPy with:

    pip install numpy

How to Run
    Run the main script with a command-line argument specifying how many prices to generate:

For Example:
    python main.py 1000
This will generate 1000 random prices using both methods and report how long each one took.

Project Structure
    price_generator_for1.py — Loop-based generator using Python’s random.

    price_generator_for2.py — NumPy-based generator.

    main.py — Runs both generators, measures execution time, and compares speed.

Sample Output
You should see output like this:

    Loop-based approach took: 0:00:03.456789

    NumPy-based approach took: 0:00:00.123456

    NumPy-based approach is faster

Notes
    The generate_random_number() function in price_generator_for1.py currently returns prices formatted with "£", suitable for display.

    The NumPy generator returns raw floats, which can be formatted as needed.

    Timing is done in the main script using a helper function to keep code clean.

    The if _name_ == "_main_": structuring ensures proper script execution.

Observation
The Loop script runs more efficiently if
    the output is simply added to a list or array.
    return is used instead of print for the output.
This also means the script is more adaptable/versatile

Possible Next Steps
    Add more complexity - generate price curves, trends, scalability, seasonality, volatility
    Data Structures - store prices in pandas DataFrames
    Forward curves - build simple price curves
    Basic valuation - calculate present values, mark-to-market
    File I/O - read/write prices to csv/excel files