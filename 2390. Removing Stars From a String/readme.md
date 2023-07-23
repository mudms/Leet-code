# LeetCode - Removing Stars From a String

## Problem

Given a string `s`, remove all occurrences of '*' characters from it.

Return the modified string.

**Example:**

Input: s = "a*bc**d*ef"
Output: "abcdef"

## Solution Approach

To solve this problem, we use a stack to process the characters in the input string `s`. We iterate through each character in the string:

- If the current character is '*', we encounter a star, so we pop the last character from the stack to remove the corresponding previous character.
- If the current character is not '*', we append it to the stack.

This way, the stack will store the characters of the string after removing the '*' characters.

Finally, we join the characters in the stack to form the modified string and return it.

## Time Complexity

The time complexity of this solution is O(n), where n is the length of the input string `s`. The algorithm iterates through each character of the string once and performs constant-time operations for each character.

## Memory Allocation

The memory allocation of this solution is O(n), where n is the length of the input string `s`. The memory is used to store the characters in the stack after removing the '*' characters.

## Note

The implementation assumes that the input `s` is a string.
