#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (64.12%)
# Likes:    11625
# Dislikes: 371
# Total Accepted:    3.1M
# Total Submissions: 4.9M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#

# @lc code=start

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
    #     # beats 90%, 65%
        if len(s) != len(t):
            return False

        s_counts = defaultdict(int)
        t_counts = defaultdict(int)
        for i in range(len(s)):
            s_counts[s[i]] += 1
            t_counts[t[i]] += 1
        if len(t_counts.keys()) == len(s_counts.keys()):
            return all({s_counts[c] == t_counts[c] for c in s_counts})
        return False

    def isAnagramAlt(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
# @lc code=end
