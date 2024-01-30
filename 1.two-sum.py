#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (51.64%)
# Likes:    54663
# Dislikes: 1853
# Total Accepted:    12.1M
# Total Submissions: 23.4M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#

# @lc code=start
class Solution:

    def binary_search(self, cur_val, n_sorted, target, l=None, r=None) -> int:
        """Search n_sorted for the index of the value where cur_val + n_sorted[i][1] == target

        Args:
            cur_val: fixed value
            n_sorted: a sorted list of values to search for a match in
            target: the target value where cur_val + n_sorted[i][1] == target
        Kwargs:
            l: the left index to start searching in
            r: the right index to start searching in

        Returns:
            match_index: the index in nums where the match was found
        """
        if l is None:
            l = 0
        if r is None:
            r = len(n_sorted) - 1
        while l <= r:
            m = (r+l) // 2
            result_val = cur_val + n_sorted[m][1]
            if result_val == target:
                return n_sorted[m][0]
            elif result_val < target:
                l = m + 1
            else:
                r = m - 1
        return None

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Hash table of complements"""
        n_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in n_map:
                return [n_map[complement], i]
            n_map[num] = i
        return None

    def twoSumBinarySearch(self, nums: List[int], target: int) -> List[int]:
        """Binary search method"""
        # beast 40%, 50%
        n_sorted = sorted([(i,n) for i, n in enumerate(nums)], key= lambda x: x[1])

        for i in range(len(n_sorted)):
            cur_val = n_sorted[i][1]
            b_search_result = self.binary_search(cur_val, n_sorted, target, l=i+1)
            if b_search_result is not None:
                return [n_sorted[i][0], b_search_result]
        return None

    def twoSumNSquared(self, nums: List[int], target: int) -> List[int]:
        """Stack method"""
        # n^2 complexity, beats 40%, 42%
        n_stack = []
        for i in range(len(nums)):
            if i != 0:
                for n in n_stack:
                    if nums[i] + n[1] == target:
                        return [n[0], i]
            n_stack.append((i, nums[i]))

# @lc code=end
