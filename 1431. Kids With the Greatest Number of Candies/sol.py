from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        x = list(set(candies))
        x.sort()
        y = x[-1]
        for candy in candies:
            if candy + extraCandies >= y:
                lst.append(True)
            else:
                lst.append(False)
        return lst

# Example usage:
if __name__ == "__main__":
    solution_obj = Solution()
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    result = solution_obj.kidsWithCandies(candies, extraCandies)
    print(result)