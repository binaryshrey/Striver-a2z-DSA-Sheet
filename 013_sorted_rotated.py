# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/submissions/1599373068/

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        drops = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1) % len(nums)]:
                drops+=1
        return drops <= 1
        