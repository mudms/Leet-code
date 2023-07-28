from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        sum = 1
        if 0 not in nums:
            for i in nums:
                sum = sum * i
            for i in nums:
                if sum == 0:
                    lst.append(sum)
                else:
                    lst.append(int(sum / i))

        if 0 in nums:
            for i in range(len(nums)):
                sum = 1
                for j in range(len(nums)):
                    if i == j:
                        continue
                    else:
                        sum = sum * nums[j]
                lst.append(sum)

        return lst

# Example usage:
if __name__ == "__main__":
    solution_obj = Solution()
    nums = [1, 2, 3, 4]
    result = solution_obj.productExceptSelf(nums)
    print(result)
