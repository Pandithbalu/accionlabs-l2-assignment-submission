"""
DigitTransformer - Computes the result of X + XX + XXX + XXXX for a given single digit X.
Example: If X = 3, output is 3 + 33 + 333 + 3333 = 3702
"""

class DigitTransformer:
    def __init__(self, digit: int):
        if not isinstance(digit, int) or digit < 0 or digit > 9:
            raise ValueError("Input must be a single decimal digit between 0 and 9.")
        self.digit = digit

    def transform(self) -> int:
        result = 0
        term = ""
        for _ in range(1, 5):
            term += str(self.digit)
            result += int(term)
        return result


if __name__ == "__main__":
    try:
        user_input = int(input("Enter a single digit (0-9): "))
        transformer = DigitTransformer(user_input)
        output = transformer.transform()
        print(f"Result of X + XX + XXX + XXXX for {user_input}: {output}")
    except ValueError as ve:
        print(f"Error: {ve}")
