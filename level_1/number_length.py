"""

Number Length Number
You have a positive integer. Try to find out how many digits it has?
Input: A positive Int

Output: An Int.

Example:
number_length(10) == 2
number_length(0) == 1

"""


def number_length(number: int = 1) -> int:
    return number


if __name__ == "__main__":
    print("Example: ")

    print(number_length(23233))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 10

    print("Coding complete")
