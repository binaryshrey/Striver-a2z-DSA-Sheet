# https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0

def frequency(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
    

print(frequency([1,2,3,1,2,2,2,3,6,4,0]))