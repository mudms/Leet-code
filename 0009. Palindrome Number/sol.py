class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

# Example usage:
if __name__ == "__main__":
    solution_obj = Solution()
    x = 121
    result = solution_obj.isPalindrome(x)
    print(result)
