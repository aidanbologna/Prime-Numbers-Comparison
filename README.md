# Prime Number Generator

A Python tool that generates prime numbers and visualizes how their values grow over count — revealing the natural sparsity of primes as numbers get larger.

![Graph showing prime number distribution](screenshot.png)

## What it does

- Generates the first *n* prime numbers using trial division
- Plots prime value vs. count, showing how gaps between primes widen over the number line
- Prints the full list of primes to the console

## Example output

Running with `n = 100` produces a curve showing the first 100 primes (up to 541), illustrating how primes become increasingly sparse.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/prime-generator.git
   cd prime-generator
   ```

2. Install dependencies:
   ```bash
   pip install matplotlib
   ```

## Usage

```bash
python primes.py <count>
```

**Example** — generate and graph the first 500 primes:
```bash
python primes.py 500
```

## How it works

For each candidate number, the algorithm checks divisibility by all odd numbers up to its square root. If none divide evenly, the number is prime. This is known as **trial division**.

- Skips even numbers entirely (after 2)
- Only checks divisors up to √n, since any factor above √n must be paired with one below it
- Uses a Python generator to yield primes one at a time, on demand

## Performance

| Count | Largest prime | Approximate time |
|-------|--------------|-----------------|
| 100 | 541 | instant |
| 1,000 | 7,919 | < 1s |
| 10,000 | 104,729 | ~1s |
| 100,000 | 1,299,709 | ~30s |

For larger ranges, a [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) would be significantly faster.

## Dependencies

- Python 3.x
- [matplotlib](https://matplotlib.org/)

## License

MIT
