"""
Problem: Majority Element II
Difficulty: Medium

Approach:
- Used Boyer-Moore Voting Algorithm [Extended]

Time Complexity: O(n)
Space Complexity: O(1)

LeetCode:
https://leetcode.com/problems/majority-element-ii/
"""
class Solution:
    def majorityElement(self, nums):
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        # First pass: find candidates
        for num in nums:
            if num == candidate1:
                count1 += 1

            elif num == candidate2:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Second pass: verify counts
        count1 = nums.count(candidate1)
        count2 = nums.count(candidate2)

        ans = []
        n = len(nums)

        if count1 > n // 3:
            ans.append(candidate1)

        if candidate2 != candidate1 and count2 > n // 3:
            ans.append(candidate2)

        return ans
