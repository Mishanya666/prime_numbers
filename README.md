# Prime_numbers
Project that finds prime numbers

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

## Table of content
- [Description](#description)
- [Installation](#installation)
- [Testing](#testing)
- [Usage](#usage)
- [License](#license)

## Description
The "Prime Numbers" project provides functions to check if a number is prime and generate prime numbers up to a given limit.
Functions:
 - is_prime(n): Checks if a number is prime.
 - generate_primes(limit): Generates a list of prime numbers up to the specified limit.

## Installation
Make sure [git](https://git-scm.com/) is installed on your system. In bash-shell execute:

    git clone https//:github.com:standlab/prime_numbers.git
    cd mtracker
    pip install .

Or simply:

    pip install git+https://github.com/Mishanya666/prime_numbers.git

## Testing
You can run tests for the project using the unittest module. Here's how to do it:
 1 Navigate to the project directory.
 2 Run the test_prime_numbers.py file.
Example
bash:

      python -m unittest my_prime_numbers.tests.test_prime_numbers

## Usage
Here's an example of how to use the project functions:

       python from my_prime_numbers.prime_numbers import is_prime, generate_primes 
       
       #Check if a number is prime 
       print(is_prime(7)) #Output: True 
       
       #Generate prime numbers up to a given limit 
       print(generate_primes(10)) #Output: [2, 3, 5, 7]


## License
The_Prime_Numbers is licensed under the terms of the MIT Open Source license and is available for free.
Now you're ready to use the "Prime Numbers" project to work with prime numbers in your applications!
