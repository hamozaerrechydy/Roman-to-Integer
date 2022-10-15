class Solution:
    def romanToInt(self, s: str) -> int:
        chars = list(s)
        nums = []
        for c in chars: 
            if c == 'I': 
                nums.append(1)
            if c == 'V': 
                nums.append(5)
            if c == 'X': 
                nums.append(10)
            if c == 'L': 
                nums.append(50)
            if c == 'C': 
                nums.append(100)
            if c == 'D': 
                nums.append(500)
            if c == 'M': 
                nums.append(1000)
        
        if nums[0] >= nums[1]:
            return sum(nums)
        elif nums[0] == 1: 
            return sum(nums) - 2
        elif nums[0] == 10 : 
            return sum(nums) - 20 
        elif nums[0] == 100 : 
            return sum(nums) - 200 
            
        
"""

Pseudocode: 
[x] create an array / list 
[x] push the chars in the arr / list 
[x] convert each char to a number and push it inside a new arr / list 
[x] if the numbers are ordred from largest to smallest return their sum 
[x] else if the first number is 1 - 10 - 100 subtract it twice from the whole sum of the nums list  

"""
