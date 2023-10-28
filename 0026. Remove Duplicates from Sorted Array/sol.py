from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1

# Example usage:
if __name__ == "__main__":
    solution_obj = Solution()
    nums = [1, 1, 2]
    result = solution_obj.removeDuplicates(nums)
    print(result)
