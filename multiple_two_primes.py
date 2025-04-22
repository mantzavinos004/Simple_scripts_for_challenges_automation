# You take a array of numbers and you take the product of the two primes 

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Read input (comma- or space-separated numbers)
n = input()
# Convert to list of integers
numbers = list(map(int, n.replace(",", " ").split()))

# Find the first two prime numbers
primes = [x for x in numbers if is_prime(x)]

# Multiply the first two primes
if len(primes) >= 2:
    key = primes[0] * primes[1]
    print(key)
else:
    print("Not enough primes!")
