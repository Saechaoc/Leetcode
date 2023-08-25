# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Since the array is sorted we know it is either a binary search or a two pointer problem. 
# two pointers, array

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

import collections

class Solution:
    # Simple solultion is to square all values then to sort
    # def sortedSquares(self,nums: list[int]) -> list[int]:
    #     newArray = [None] * len(nums)

    #     for idx in range(len(nums)):
    #         newArray[idx] = nums[idx] ** 2
        
    #     return sorted(newArray)
    
    #O(n) solution using two pointers, we know that the right most value will always be the biggest
    #We are using pos instead of insert since its an O(1) operation.
    def sortedSquares(self,nums: list[int]) -> list[int]:
        right = pos = len(nums) - 1
        newArray = [0] * len(nums)
        left = 0

        while left <= right:
            if abs(nums[right]) >= abs(nums[left]):
                newArray[pos] = nums[right] ** 2
                right -= 1
            else:
                newArray[pos] = nums[left] ** 2
                left += 1
            pos -= 1
        return newArray
    
sln = Solution()

nums = [-4,-1,0,3,10]
output = [0,1,9,16,100]

# print(sln.sortedSquares(nums))
print(output == sln.sortedSquares(nums))

nums = [-7,-3,2,3,11]
output = [4,9,9,49,121]
print(output == sln.sortedSquares(nums))