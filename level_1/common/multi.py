"""

This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO
and how to get the most out of solving them.
As you solve missions more stations become available to you, containing more complex missions.

This mission is the easiest one.
Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.

Input: Two arguments. Both are of type int.

Output: Int.

Example:
mult_two(2, 3) == 6
mult_two(1, 0) == 0
1
2

"""


def multi_two_nr(a: int = 0, b: int = 0):
    return a * b


if __name__ == "__main__":
    print("Example: ")
    print(multi_two_nr())

    # These "asserts" are used for self-checking and not for an auto-testing

    assert multi_two_nr(3, 2) == 6
    assert multi_two_nr(1, 0) == 0
    print("Coding complete!")
