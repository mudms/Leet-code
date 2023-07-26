# LeetCode - Reverse Vowels of a String

## Problem

Given a string `s`, reverse only the vowels of the string and return the modified string.

The vowels are 'a', 'e', 'i', 'o', and 'u' (case-insensitive), and the input string will only consist of lowercase and uppercase letters.

**Example:**

Input: s = "hello"
Output: "holle"

## Solution Approach

To solve this problem, we first identify the vowels in the input string `s` and store them in a list called `lst`.

We also create an empty list called `word`, which will store the characters of the string after the vowel reversal.

We iterate through each letter in the string `s` and append it to the `word` list. If the letter is a vowel, we also append it to the `lst`.

After obtaining the `lst` with all the vowels in reverse order, we again iterate through each letter in the string `s`. If the letter is a vowel, we replace it with the last vowel from the `lst` and remove that vowel from the list.

Finally, we join the characters in the `word` list to form the modified string and return it.

## Time Complexity

The time complexity of this solution is O(n), where n is the length of the input string `s`. The algorithm iterates through the string twice: once to find the vowels and once to reverse them.

## Memory Allocation

The memory allocation of this solution is O(n), where n is the length of the input string `s`. The memory is used to store the `lst` and `word` lists, each of which can have a maximum size of n.

## Note

The implementation assumes that the input `s` is a string containing only lowercase and uppercase letters.
