# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
# This looks like a two pointer problem
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.
# Example 2:

# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

class Solution:
    #While this approach is ok, you can speed it up by using a binary search for larger arrays since n1 & n2 are sorted
    def minimumCommon(self, nums1: list[int], nums2: list[int]) -> int:
        leftPointer = 0
        rightPointer = 0

        while leftPointer < len(nums1) and rightPointer < len(nums2):
            if nums1[leftPointer] > nums2[rightPointer]:
                rightPointer += 1
            elif nums1[leftPointer] < nums2[rightPointer]: #[3,4,6], [1,2,3]
                leftPointer += 1
            else:
                return nums1[leftPointer]
        return -1

soln = Solution()

nums1 = [1,2,3]
nums2 = [2,4]
print(soln.minimumCommon(nums1,nums2))
Output = 2

nums1 = [1,2,3,6]
nums2 = [2,3,4,5]
Output = 2