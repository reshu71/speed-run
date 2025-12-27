"""Module providing a function printing python version."""

import sys

def factorial(n):
    result = 1
    # Loop from 1 to n (inclusive?)
    for i in range(1, n+1): 
        result = result * i
    return result

def main():
    # If an argument is provided, use it. Otherwise default to 5.
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = 5
        
    print(f"Calculating factorial of {number}...")
    calc = factorial(number)
    print(f"The factorial of {number} is {calc}")

if __name__ == "__main__":
    main()


#  Key "Advanced" Concepts here:

# "request": "launch": We are starting the app. (vs "attach", where you connect to a running server).

# "${file}": A variable that resolves to whatever file you have open.

# "justMyCode": true: Critical. This tells the debugger to skip over Python's internal libraries (like os or sys) and only stop in your code.   