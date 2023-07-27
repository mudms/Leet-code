class Solution:
    def reverseWords(self, s: str) -> str:
        line = s.split(" ")
        lst = []
        for i in range(-1, -len(line) - 1, -1):
            if line[i] == '':
                continue
            lst.append(line[i])
        x = " "
        return x.join(lst)

# Example usage:
if __name__ == "__main__":
    solution_obj = Solution()
    input_string = "  hello world  "
    result = solution_obj.reverseWords(input_string)
    print(result)
