# https://leetcode.com/problems/reverse-integer/description/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_no = 0
        if x < -2**31 or x > 2**31 - 1:
            return 0

        if x < 0:
            no = str(x)[1:]
            reverse_no = int("-"+no[::-1])
             
        else:
            reverse_no = int(str(x)[::-1])

        if reverse_no < -2**31 or reverse_no > 2**31 - 1:
            return 0

        return reverse_no
            
        