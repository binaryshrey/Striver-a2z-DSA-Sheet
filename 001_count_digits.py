# https://www.naukri.com/code360/problems/count-digits_8416387

import math

def count_digits(n):
    count = int(math.log10(n)+1)
    return count
    
print(count_digits(2432324241))