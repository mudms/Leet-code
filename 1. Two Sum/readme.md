# LeetCode - Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

## Solution Approach

The problem requires finding two numbers in the array that add up to the given target. We can use a two-pointer approach to solve this problem efficiently. The two-pointer approach involves initializing two pointers, `left` and `right`, at the beginning and end of the sorted array, respectively.

1. Sort the array `nums` in ascending order.
2. Initialize two pointers, `left` at the start (index 0) and `right` at the end (index len(nums) - 1) of the array.
3. While `left` is less than `right`, calculate the sum of elements at `left` and `right`.
   - If the sum is equal to the `target`, return the indices [left, right].
   - If the sum is less than the `target`, increment `left` to explore larger elements.
   - If the sum is greater than the `target`, decrement `right` to explore smaller elements.
4. If no such pair is found, return an empty list.

## Time Complexity

The time complexity of the two-pointer approach used in this solution is O(n log n), where n is the number of elements in the input array `nums`. The time complexity is dominated by the sorting step, which takes O(n log n) time using efficient sorting algorithms.

## Memory Allocation

The memory allocation of this solution is O(n), where n is the number of elements in the input array `nums`. This memory is used to store the sorted array.

## Note

This problem can also be solved using a hashmap (dict) to achieve a linear time complexity of O(n) without the need for sorting. However, the two-pointer approach described in this solution still offers a reasonably efficient solution.
