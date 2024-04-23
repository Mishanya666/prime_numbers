# prime_numbers
Project that finds prime numbers

# Description
The "Prime Numbers" project provides functions to check if a number is prime and generate prime numbers up to a given limit.
Functions:
 • is_prime(n): Checks if a number is prime.
 • generate_primes(limit): Generates a list of prime numbers up to the specified limit.

# Installation
You can install the project using pip, using the GitHub link:
bash


pip install git+https://github.com/yourusername/my_prime_numbers_project.git
# Testing
You can run tests for the project using the unittest module. Here's how to do it:
 1 Navigate to the project directory.
 2 Run the test_prime_numbers.py file.
Example:
bash


python -m unittest my_prime_numbers.tests.test_prime_numbers
# Usage
Here's an example of how to use the project functions:
python


from my_prime_numbers.prime_numbers import is_prime, generate_primes # Check if a number is prime print(is_prime(7)) # Output: True # Generate prime numbers up to a given limit print(generate_primes(10)) # Output: [2, 3, 5, 7]
Now you're ready to use the "Prime Numbers" project to work with prime numbers in your applications!
