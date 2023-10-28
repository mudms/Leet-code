# LeetCode - Remove Duplicates from Sorted Array

## Problem

Given a sorted array `nums`, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

**Example:**

Input: nums = [1,1,2]
Output: 2

## Solution Approach

To remove duplicates from a sorted array in-place, we can use two pointers:

- Initialize two pointers `i` and `j` at the beginning of the array.
- Iterate through the array with the `j` pointer.
- If `nums[i]` is not equal to `nums[j]`, increment `i` and update `nums[i]` with `nums[j]`.
- Continue this process until `j` reaches the end of the array.
- The length of the array without duplicates is `i + 1`.

## Time Complexity

The time complexity of this solution is O(n), where n is the length of the input array `nums`. Both pointers traverse the array once.

## Memory Allocation

The memory allocation of this solution is O(1). The algorithm uses a constant amount of memory for variables and pointers.

## Note

The implementation assumes that the input `nums` is a sorted list of integers.
