"""
Problem: Contains Duplicate
Difficulty: Easy

Approach:
- Use HashSet to check the duplication of numbers.

Time Complexity: O(n)
Space Complexity: O(n)

LeetCode:
https://leetcode.com/problems/contains-duplicate/
"""

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
