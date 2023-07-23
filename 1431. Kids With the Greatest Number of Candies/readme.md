# LeetCode - Kids With the Greatest Number of Candies

## Problem

Given the array `candies` representing the number of candies that each kid has and the integer `extraCandies`, where extraCandies[i] represents the number of extra candies that the ith kid has.

Return a boolean array `res` of length `n`, where res[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids. Otherwise, res[i] is false.

A kid must have at least one candy, even if they have no extra candies.

**Example:**

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]

## Solution Approach

To solve this problem, we find the maximum number of candies that any kid has in the list `candies`. Then, we iterate through each kid's candies and check if giving them the `extraCandies` would make them have the greatest number of candies among all kids.

We create an empty list `lst` to store the boolean results for each kid. We use the `max` function to find the maximum number of candies in `candies` and store it in the variable `y`.

Next, we iterate through each kid's candies in `candies`. For each kid's candy count, we compare it with `y + extraCandies`.

- If the kid's candy count plus `extraCandies` is greater than or equal to `y`, we append `True` to the `lst`.
- Otherwise, we append `False` to the `lst`.

Finally, we return the `lst`.

## Time Complexity

The time complexity of this solution is O(n), where n is the number of kids represented by the list `candies`. We iterate through `candies` once to find the maximum candy count and then iterate again to determine if each kid has the greatest number of candies.

## Memory Allocation

The memory allocation of this solution is O(n), where n is the number of kids represented by the list `candies`. The memory is used to store the result list `lst`.

## Note

The implementation assumes that the input `candies` is a list of integers and `extraCandies` is an integer.
