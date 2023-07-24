# LeetCode - Can Place Flowers

## Problem

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer list `flowerbed` containing 0's and 1's, where 0 means an empty plot, and 1 means a planted flower, and an integer `n`, return if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

**Example:**

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

## Solution Approach

To solve this problem, we traverse the `flowerbed` list and check if we can plant a new flower at each plot. We maintain a count `n` to keep track of the number of flowers to be planted.

If `n` is already zero, it means we have successfully planted all the required flowers without violating the no-adjacent-flowers rule, so we return `True`.

The function iterates through the `flowerbed` list and checks each plot to determine if it can be used for planting. The following conditions are checked:

- If the current plot is 0 (empty) and both its adjacent plots (if present) are also empty (0), we can plant a flower in this plot. We decrement `n` to indicate that we have planted a flower.
- If `n` becomes zero during the iteration, it means we have successfully planted all the required flowers, and we return `True`.
- If we reach the end of the iteration and `n` is still greater than zero, it means we cannot plant all the required flowers, and we return `False`.

## Time Complexity

The time complexity of this solution is O(N), where N is the number of elements in the `flowerbed` list. We traverse the list once to determine if we can plant the flowers.

## Memory Allocation

The memory allocation of this solution is O(1). The algorithm uses a constant amount of memory to store the variables `n` and the loop index.

## Note

The implementation assumes that the input `flowerbed` is a list of integers (0's and 1's) and `n` is an integer.
