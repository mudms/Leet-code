# LeetCode - Median of Two Sorted Arrays

## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log(min(m,n))).

**Example:**

Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0

## Solution Approach

To find the median of two sorted arrays efficiently, we can merge the arrays into a single sorted array and then calculate the median.

- Merge the two arrays `nums1` and `nums2` into a new array `arr`.
- Sort the merged array.
- If the length of the merged array `arr` is even, calculate the median by taking the average of the middle two elements.
- If the length is odd, the median is the middle element.

## Time Complexity

The time complexity of this solution is O((m + n) log(m + n)), where m and n are the lengths of the arrays `nums1` and `nums2`. This is due to the sorting step.

## Memory Allocation

The memory allocation of this solution is O(m + n), where m and n are the lengths of the arrays `nums1` and `nums2`. This is the space required for the merged array.

## Note

The implementation assumes that the input `nums1` and `nums2` are lists of integers.
