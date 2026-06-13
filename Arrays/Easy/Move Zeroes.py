"""
Problem: Move Zeroes
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

LeetCode:
https://leetcode.com/problems/move-zeroes/
"""
class Solution:
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
