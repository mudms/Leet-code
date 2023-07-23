# LeetCode - Count Equal Pairs in a Grid

## Problem

You are given a 2D grid of integers called `grid`. Each row in the grid represents a pair, and each element in the row represents an integer value. Your task is to count the number of pairs in the grid such that the rows and columns have the same set of integers.

Return the total number of equal pairs.

**Example:**

Input:
grid = [
    [3, 2, 1],
    [1, 7, 6],
    [2, 7, 7]
]

Output: 1

Explanation: In this example, there is one pair that satisfies the condition:
- Row 2 and Column 1 have the same set of integers [2, 7, 7].

## Solution Approach

To solve this problem, we use a dictionary to store the frequency of rows. We iterate through the grid, convert each row to a tuple (immutable), and store it in the dictionary as the key, with the value being the frequency of that row.

Next, we create a list to store the counts of columns that match the rows. We use the zip function to iterate through the grid column-wise, convert each column to a tuple, and check how many times that column appears in the dictionary.

Finally, we return the sum of the counts from the list.

## Time Complexity

The time complexity of this solution is O(N * M), where N is the number of rows and M is the number of columns in the grid. The time complexity is dominated by the iteration through the grid to count the frequency of rows and columns.

## Memory Allocation

The memory allocation of this solution is O(N * M), where N is the number of rows and M is the number of columns in the grid. The memory is used to store the dictionary and the list of column counts.

## Note

The implementation assumes that the input grid is a 2D list of integers.
