"""
EvenFibonacciSum - Calculate the sum of the first 100 even-valued Fibonacci numbers.
"""

class EvenFibonacciSum:
    def __init__(self, count: int):
        self.count = count

    def calculate_sum(self) -> int:
        even_fibs = []
        a, b = 0, 1
        while len(even_fibs) < self.count:
            a, b = b, a + b
            if a % 2 == 0:
                even_fibs.append(a)
        return sum(even_fibs)


if __name__ == "__main__":
    fib_counter = EvenFibonacciSum(100)
    result = fib_counter.calculate_sum()
    print(f"Sum of first 100 even Fibonacci numbers: {result}")
