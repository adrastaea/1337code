#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
from collections import defaultdict
# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        if len(points) == 1:
            return 1

        def get_slope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            if dx == 0: return float('inf')
            if dy == 0: return 0
            return dy / dx

        def get_y_intercept(p, slope):
            if slope == float('inf'):
                return (slope, p1[0])
            return p[1] - slope * p[0]

        def get_line_tuple(p1, p2):
            slope = get_slope(p1, p2)
            return (slope, get_y_intercept(p1, slope))

        max_points = 0
        for i, p1 in enumerate(points):
            lines = defaultdict(int)
            for p2 in points[i+1:]:
                line_tuple = get_line_tuple(p1, p2)
                lines[line_tuple] += 1
            max_points = max(max_points, max(lines.values(), default=0) + 1)
        return max_points
# @lc code=end
