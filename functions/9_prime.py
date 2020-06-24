"""
9. Write a Python function that takes a number as a parameter and check the
number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that
has no positive divisors other than 1 and itself.
"""


def check_if_prime(num):
    if num < 5:
        for i in range(2, num):
            if num % i == 0:
                return f"{num} is not a prime number."
    else:
        for i in range(2, (num//2)):
            if num % i == 0:
                return f"{num} is not a prime number."
    return f'{num} is a prime number.'


print(check_if_prime(4))
