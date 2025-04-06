# https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1

import math

class Solution:
    
    def allDivisors(self, n):
        divisors = []
        srqtN = int(math.sqrt(n))
        for i in range(1, srqtN + 1):
            if n % i == 0:
                divisors.append(i)
                if n // i != i:
                    divisors.append(n // i)
        print(n, (divisors))
        return sum(divisors)
        
    def sumOfDivisors(self, n):
        # code here
        total_sum = 0
        for i in range(1, n + 1):
            total_sum += self.allDivisors(i)
        return total_sum

sol = Solution()
print(sol.sumOfDivisors(4))
