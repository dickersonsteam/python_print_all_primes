import time


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def is_divisible(x, divisor):
    if x % divisor == 0:
        return True
    else:
        return False


def is_prime(x):
    if x == 2:  # 2 is the only even prime
        return True
    elif x < 2 or is_even(x): # all other primes are odd
        return False
    else:  # start with 3 and increment by 2 to skip even numbers.
        for test in range(3, x, 2):
            if is_divisible(x, test):
                return False
    return True


# Print 2 now to save time later
print("2")

# Start with the first odd prime
# Increment by two to skip even numbers
number = 3

# Forever loop
while True:

    # Print the number only if it is prime.
    if is_prime(number):
        print(number)

    # Increment by two to skip even numbers
    number += 2

    # Slow things down for testing.
    time.sleep(.5)