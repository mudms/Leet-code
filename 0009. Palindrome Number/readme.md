# LeetCode - Palindrome Number

## Problem

Determine whether an integer `x` is a palindrome. An integer is a palindrome when it reads the same backward as forward.

An example of a palindrome is 121.

**Example:**

Input: x = 121
Output: true

## Solution Approach

To check if an integer is a palindrome, we convert it to a string and compare it with its reverse.

- Convert the integer `x` to a string.
- Check if the string is equal to its reverse (`x[::-1]`).
- If they are equal, return `True`; otherwise, return `False`.

## Time Complexity

The time complexity of this solution is O(n), where n is the number of digits in the integer `x`. Converting an integer to a string takes O(n) time, and comparing two strings takes O(n) time.

## Memory Allocation

The memory allocation of this solution is O(n), where n is the number of digits in the integer `x`. This is the space required for the string conversion.

## Note

The implementation assumes that the input `x` is an integer.
