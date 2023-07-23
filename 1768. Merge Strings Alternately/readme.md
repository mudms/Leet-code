# LeetCode - Merge Strings Alternately

## Problem

You are given two strings `word1` and `word2`.

Merge the strings alternately, starting with `word1`. If one string is longer than the other, append the remaining characters of the longer string at the end of the merged string.

Return the merged string.

**Example:**

Input: word1 = "abc", word2 = "def"
Output: "adbecf"

## Solution Approach

To solve this problem, we can use a simple loop to merge the two strings alternately. We initialize two pointers `i` and `j` to 0 to keep track of the current index in `word1` and `word2`, respectively.

We also initialize an empty list `lst` to store the characters of the merged string.

We loop while both `word1` and `word2` have remaining characters. In each iteration, we append the current characters at index `i` from `word1` and index `j` from `word2` to the `lst`. Then, we increment `i` and `j` to move to the next character in each string.

After the loop, if there are remaining characters in `word1` or `word2`, we append them to the `lst` to include all remaining characters.

Finally, we join the characters in the `lst` to form the merged string and return it.

## Time Complexity

The time complexity of this solution is O(N + M), where N is the length of `word1` and M is the length of `word2`. The algorithm iterates through both strings once to merge them alternately.

## Memory Allocation

The memory allocation of this solution is O(N + M), where N is the length of `word1` and M is the length of `word2`. The memory is used to store the characters in the `lst` after merging the two strings.

## Note

The implementation assumes that the inputs `word1` and `word2` are strings.
