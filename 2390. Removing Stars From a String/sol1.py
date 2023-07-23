class Solution:
    def removeStars(self, s: str) -> str:
        lst = []
        count = 0

        for i in range(-1, -len(s) - 1, -1):
            if s[i] == '*':
                count += 1
                continue
            if count > 0:
                count -= 1
                continue
            else:
                lst.append(s[i])

        lst.reverse()

        return "".join(lst)

# Example usage:
if __name__ == "__main__":
    input_string = "leet**cod*e"
    solution_obj = Solution()
    result = solution_obj.removeStars(input_string)
    print(result)
