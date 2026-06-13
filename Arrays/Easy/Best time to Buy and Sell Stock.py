"""
Problem: Best time to Buy and Sell Stock.oy
Difficulty: Easy

Approach:
- Used Greedy Approach

Time Complexity: O(n)
Space Complexity: O(1)

LeetCode:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock.oy/
"""
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
