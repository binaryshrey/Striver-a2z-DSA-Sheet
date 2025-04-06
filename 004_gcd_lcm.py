# https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1

import math

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # while a>0 and b>0:
        #     if a>b:
        #         a = a%b
        #     else:
        #         b = b%a
            
        # if a == 0:
        #     return b
        # return a
        
        return [int(abs(a*b)//math.gcd(a,b)), math.gcd(a,b)]