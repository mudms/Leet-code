class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        lst = []
        i = 0
        x = True
        while x:
            lst.append(word1[i])
            lst.append(word2[i])
            i += 1
            word1_len -= 1
            word2_len -= 1

            if word1_len == 0 or word2_len == 0:
                x = False
        if word1_len > word2_len:
            lst.append(word1[i - len(word1)::1])
        if word1_len < word2_len:
            lst.append(word2[i - len(word2)::1])
        op_str = ""
        
        return op_str.join(lst)

# Example usage:
if __name__ == "__main__":
    solution_obj = Solution()
    word1 = "abc"
    word2 = "def"
    result = solution_obj.mergeAlternately(word1, word2)
    print(result)
