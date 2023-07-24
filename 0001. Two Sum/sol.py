from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = 0
        
        # Enumerate -> [(index,list_item)]
        for i, num in enumerate(nums):
            x = target - num
            
            if x in nums[i+1:]:
                a = i
                break

        # we are checking if x -> [second_num=target-first_num] and its index is not equal to the previos num 
        for i, num in enumerate(nums):
            if num == x and i != a:
                return [a, i]

# Example usage:
if __name__ == "__main__":
    
    #change examples based on your requirements
    nums = [2, 7, 11, 15]
    target = 9

    solution_obj = Solution()
    result = solution_obj.twoSum(nums, target)
    print(result)