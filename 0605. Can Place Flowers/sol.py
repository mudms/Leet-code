from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i + 1] != 1:
                    n -= 1
                    flowerbed[i] = 1
                elif i == (len(flowerbed) - 1) and flowerbed[i - 1] != 1:
                    n -= 1
                    flowerbed[i] = 1
                elif i == 0 or i == len(flowerbed) - 1:
                    continue
                elif flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1:
                    n -= 1
                    flowerbed[i] = 1
            if n == 0:
                return True
        return False

# Example usage:
if __name__ == "__main__":
    solution_obj = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    result = solution_obj.canPlaceFlowers(flowerbed, n)
    print(result)
