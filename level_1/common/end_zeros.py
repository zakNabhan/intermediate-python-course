"""

Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.

Example:
end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0

"""


def end_zeros(number: int) -> int:
    n = str(number)
    return len(n) - len(n.strip('0'))


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(10))

    # These "asserts" are used for self-checking and not for an auto-testing

    print("Coding complete? Click 'Check' to earn cool rewards!")
