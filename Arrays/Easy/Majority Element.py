"""
Problem: Majority Element
Difficulty: Easy

Approach:
- Used Hashing.

Time Complexity: O(n)
Space Complexity: O(1)

LeetCode:
https://leetcode.com/problems/majority-element/
"""
class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if num == candidate else -1

        return candidate
