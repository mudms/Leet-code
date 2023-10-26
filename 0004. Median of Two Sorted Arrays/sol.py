from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        x = len(arr)
        if x % 2 == 0:
            return float(0.5 * (arr[x // 2 - 1] + arr[x // 2]))
        else:
            return float(1.0 * arr[x // 2])

# Example usage:
if __name__ == "__main__":
    solution_obj = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    result = solution_obj.findMedianSortedArrays(nums1, nums2)
    print(result)
