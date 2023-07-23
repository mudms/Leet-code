# LeetCode - Removing Stars From a String

## Problem

Given a string `s`, remove all occurrences of '*' characters from it.

Return the modified string.

**Example:**

Input: s = "a*bc**d*ef"
Output: "abcdef"

## Solution Approach

To solve this problem, we use a list to store the characters of the string `s` after removing the '*' characters. We iterate through the string from the end using a reversed loop. When we encounter a '*', we skip it and increment a count. If we encounter a non-asterisk character and the count is greater than 0, we decrement the count to skip removing the corresponding '*' character. Otherwise, we add the character to the list.

After processing all characters, we reverse the list to obtain the correct order of characters and return the modified string.

## Time Complexity

The time complexity of this solution is O(n), where n is the length of the input string `s`. The algorithm iterates through the string once from the end, performing constant-time operations in each iteration.

## Memory Allocation

The memory allocation of this solution is O(n), where n is the length of the input string `s`. The memory is used to store the list of characters after removing the '*' characters.

## Note

The implementation assumes that the input `s` is a string.
