# LeetCode - Roman to Integer

## Problem

Given a roman numeral `s`, convert it to an integer.

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D`, and `M`.

- `I`: 1
- `V`: 5
- `X`: 10
- `L`: 50
- `C`: 100
- `D`: 500
- `M`: 1000

For example, the numeral `II` is two, and `IX` is nine. There are some special rules to be aware of:

- Two letters that are the same next to each other are added together.
- If a smaller numeral appears before a larger numeral, it is subtracted. For example, `IV` is 4.

**Example:**

Input: s = "III"
Output: 3

## Solution Approach

To convert a Roman numeral to an integer, we iterate through the characters of the string and sum the corresponding values. However, if a smaller numeral appears before a larger numeral, we subtract the smaller numeral.

- Initialize a dictionary `nums` to map Roman numerals to their integer values.
- Initialize a variable `num` to store the result.
- Iterate through the characters of the string.
- If the value of the current numeral is less than the value of the next numeral, subtract it from the total.
- Otherwise, add it to the total.
- Return the total.

## Time Complexity

The time complexity of this solution is O(n), where n is the length of the input string `s`.

## Memory Allocation

The memory allocation of this solution is O(1). The algorithm uses a constant amount of memory for variables and the dictionary.

## Note

The implementation assumes that the input `s` is a valid Roman numeral.
