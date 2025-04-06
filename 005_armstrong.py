# https://leetcode.com/problems/armstrong-number/description/

import math
class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        no = n
        sum = 0
        digit_count = int(math.log10(n)+1)
        while(n>0):
            digit = n%10
            sum += digit**digit_count
            n = n//10
        if(no == sum):
            return True
        else:
            return False

        