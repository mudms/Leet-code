from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        # Creating a defaultdict d[value]=0 untill specified otherwise
        d = defaultdict(int)
        
        # We add rows of the grid such to the dict such that ->if not unqiue double the value of the item else initalise at 1 
        for row in grid:
            d[tuple(row)] += 1

        
        #intitalise a empty list
        lst = list()

        # zip(*grip) unzips the grid ie. all the items are returned as tuples of there respective index in the list
        # zip(*grip) in Python is a one-liner that transposes the elements of the iterable grip
        for col in zip(*grid):

            # we append the value of the item-> col such that if present in d then its respective value is appended in the list or else '0' is appended 
            lst.append(d[tuple(col)])

        # We take the sum of the list 
        return sum(lst)

# Example usage:
if __name__ == "__main__":
    grid = [
        [3, 2, 1],
        [1, 7, 6],
        [2, 7, 7]
    ]

    solution_obj = Solution()
    result = solution_obj.equalPairs(grid)
    print(result)
