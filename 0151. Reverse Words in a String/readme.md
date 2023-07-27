# LeetCode - Reverse Words in a String

## Problem

Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

A word is defined as a sequence of non-space characters. The input string does not contain leading or trailing spaces, and the words are always separated by a single space.

**Example:**

Input: s = "Let's reverse words"
Output: "s'teL esrever sdrow"

## Solution Approach

To solve this problem, we first split the input string `s` into individual words using the space character as the delimiter. We obtain a list of words called `line`.

Next, we initialize an empty list called `lst`, which will store the reversed words.

We then iterate through the `line` list in reverse order using a for loop. For each word in the `line`, we check if it is an empty string (possible when there are multiple spaces between words) and skip it. Otherwise, we append the reversed word to the `lst`.

After iterating through all the words, we join the words in the `lst` list using a single space as the separator to form the modified string and return it.

## Time Complexity

The time complexity of this solution is O(n), where n is the length of the input string `s`. The algorithm splits the string into words and iterates through each word once to reverse them.

## Memory Allocation

The memory allocation of this solution is O(n), where n is the length of the input string `s`. The memory is used to store the `line` list of words and the `lst` list of reversed words.

## Note

The implementation assumes that the input `s` is a string containing words separated by a single space and no leading/trailing spaces.
