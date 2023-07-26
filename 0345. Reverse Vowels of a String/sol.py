class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        lst = []
        word = []
        for letter in s:
            word.append(letter)
            if letter in vowels:
                lst.append(letter)

        for i in range(len(s)):
            if s[i] in vowels:
                word[i] = lst[-1]
                lst.pop()

        x = ""
        return x.join(word)

# Example usage:
if __name__ == "__main__":
    solution_obj = Solution()
    input_string = "hello"
    result = solution_obj.reverseVowels(input_string)
    print(result)
