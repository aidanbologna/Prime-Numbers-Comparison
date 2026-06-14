import matplotlib.pyplot as plt
import sys

n = int(sys.argv[1])

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime_generator():
    yield 2
    num = 3
    while True:
        if is_prime(num):
            yield num
        num += 2

gen = prime_generator()
primes = [next(gen) for _ in range(n)]

plt.figure(figsize=(10, 5))
plt.title(f'First {n} primes — count vs value')
plt.xlabel('Prime value')
plt.ylabel('Count (nth prime)')
plt.plot(primes, range(n))
plt.tight_layout()
plt.show()