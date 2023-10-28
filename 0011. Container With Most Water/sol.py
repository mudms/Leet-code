from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        ans = 0
        while i <= j:
            ans = max(ans, (min(height[i], height[j]) * (j - i)))

            if height[j] > height[i]:
                i += 1
            else:
                j -= 1

        return ans

# Example usage:
if __name__ == "__main__":
    solution_obj = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = solution_obj.maxArea(height)
    print(result)
