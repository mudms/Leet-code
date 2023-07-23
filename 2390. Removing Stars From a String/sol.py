class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == '*': 
                stack.pop()
            else: 
                stack.append(i)
        return ''.join(stack)

# Example usage:
if __name__ == "__main__":
    input_string = "leet**cod*e"
    solution_obj = Solution()
    result = solution_obj.removeStars(input_string)
    print(result)
