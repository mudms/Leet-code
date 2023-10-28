# LeetCode - Container With Most Water

## Problem

Given `n` non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

**Example:**

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

## Solution Approach

To find the container with the most water, we use a two-pointer approach:

- Initialize two pointers `i` and `j` at the beginning and end of the array.
- Calculate the area between the lines at `height[i]` and `height[j]`.
- Move the pointers toward each other. If `height[i]` is smaller than `height[j]`, move `i` to the right. Otherwise, move `j` to the left.
- Update the maximum area if the current area is greater.

Repeat the process until `i` and `j` meet.

## Time Complexity

The time complexity of this solution is O(n), where n is the number of elements in the `height` array. Both pointers traverse the array once.

## Memory Allocation

The memory allocation of this solution is O(1). The algorithm uses a constant amount of memory for the pointers and variables.

## Note

The implementation assumes that the input `height` is a list of non-negative integers.
