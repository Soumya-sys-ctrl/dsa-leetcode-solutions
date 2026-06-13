"""
Problem: Best Time to Buy and Sell Stock II.py
Difficulty: Medium

Approach:
- Used Greedy Approach

Time Complexity: O(n)
Space Complexity: O(1)

LeetCode:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
