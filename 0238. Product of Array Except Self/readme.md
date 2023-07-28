# LeetCode - Product of Array Except Self

## Problem

Given an array `nums` of n integers, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

**Example:**

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

## Solution Approach

To solve this problem without using the division operation and in O(n) time complexity, we need to calculate the product of all elements except the current element in the array.

We first check if the array `nums` contains a 0 element. If it doesn't, we can easily calculate the product of all elements using a single pass and then divide it by each element to get the output.

If `nums` contains a 0, we need to handle it separately. For each element in `nums`, we can calculate the product of all elements except the current element by multiplying all elements except the element at the current index. This can be done using two nested loops.

The first loop iterates over the `nums` array, and for each element at index `i`, the second loop iterates over the `nums` array again, excluding the element at index `i`. During this process, we calculate the product of all elements except the current element and store it in the output list.

Finally, we return the output list containing the product of all elements except each element in `nums`.

## Time Complexity

The time complexity of this solution is O(n), where n is the number of elements in the `nums` array. The algorithm iterates through the array twice (in the case of a 0 element) or once (in the case of no 0 element).

## Memory Allocation

The memory allocation of this solution is O(n), where n is the number of elements in the `nums` array. The memory is used to store the output list.

## Note

The implementation assumes that the input `nums` is a list of integers.
