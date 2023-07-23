# LeetCode - Greatest Common Divisor of Strings

## Problem

You are given two strings `str1` and `str2`.

Find the greatest common divisor of the strings.

A string `s` is a divisor of string `t` if there exists a string `u` such that `t = s + u`.

If there are multiple solutions, return the longest one. If there are no solutions, return an empty string.

**Example:**

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

## Solution Approach

To solve this problem, we define a recursive function `gcd(str1, str2)` that calculates the greatest common divisor of two strings.

The function first checks if the length of `str1` is smaller than `str2`. If it is, it swaps the arguments and calls itself again to ensure that `str1` is always larger than or equal to `str2`.

Next, the function checks if `str1` does not start with `str2`. If it doesn't, it means `str2` is not a divisor of `str1`, and the function returns an empty string.

If `str2` is empty (length 0), it means `str1` is divisible by `str2`, and the function returns `str1`.

Otherwise, the function recursively calls itself with the substring of `str1` starting after the `str2` length and the original `str2`.

The function returns the greatest common divisor of the two strings.

The main function, `gcdOfStrings`, simply calls the `gcd` function with the provided `str1` and `str2`.

## Time Complexity

The time complexity of this solution is O(n), where n is the length of the longest string between `str1` and `str2`. In the worst case, the `gcd` function performs n recursive calls.

## Memory Allocation

The memory allocation of this solution is O(n), where n is the length of the longest string between `str1` and `str2`. The memory is used for the recursive function call stack.

## Note

The implementation assumes that the inputs `str1` and `str2` are strings.
