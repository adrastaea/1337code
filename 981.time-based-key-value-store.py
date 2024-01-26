#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

from collections import defaultdict

# @lc code=start
class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        tlist = self.tmap.get(key)
        # print(f"Tlist[{key}][{timestamp}] = {tlist}")
        if not tlist:
            return ""
        elif tlist[0][0] > timestamp:
            return ""
        elif tlist[-1][0] <= timestamp:
            return tlist[-1][1]
        elif len(tlist) == 1:
            return tlist[0][1]

        l = 0
        r = len(tlist) - 1
        while l <= r:
            m = (r + l) // 2

            if tlist[m][0] == timestamp:
                return tlist[m][1]
            elif tlist[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1

        return tlist[l-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
