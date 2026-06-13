"""
Problem: Product of Array Expect Self
Difficulty: Edium 

Approach:
- Used Prefix & suffix Arrays

Time Complexity: O(n)
Space Complexity: O(1) [Excluding output array]

LeetCode:
https://leetcode.com/problems/product-of-array-except-self/
"""
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
