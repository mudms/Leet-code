class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(str1, str2):
            if len(str1) < len(str2):
                return gcd(str2, str1)
            elif not str1.startswith(str2):
                return ""
            elif len(str2) == 0:
                return str1
            else:
                return gcd(str1[len(str2):], str2)

        return gcd(str1, str2)

# Example usage:
if __name__ == "__main__":
    solution_obj = Solution()
    str1 = "ABCABC"
    str2 = "ABC"
    result = solution_obj.gcdOfStrings(str1, str2)
    print(result)
