"""
Given an integer array of even length arr, 
return true 
if it is possible to reorder arr such that 
arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, 
or false otherwise.

arr has even length
arr[2*i + 1] = 2 * arr[2 * i]

[4,-2,2,-4] -> len = 4
0 <= i < 2
i = 0, 1
[-2, -4, 2, 4]
arr[2 * 0 + 1] = 2 * arr[2 * 0], => arr[1] = 2 * arr[0], true
arr[2 * 1 + 1] = 2 * arr[2 * 1], => arr[3] = 2 * arr[2], true

every element has to be twice as great as the element before it
so (0,1), (2, 3), (4,5), and so on

2 <= arr.length <= 3 * 10^4 -> medium size
arr.length is even
10^5 <= arr[i] <= 10^5 -> big

we don't have to make array, just make sure it is possible
maybe use a map for pairs?

doesn't say if arr[i] is unique, so there could be duplicates
sort the array? 

we can use a frequency map
key -> number, value -> count of that number in array

fast lookup of doubles through keys and then we can sort the list by absolute value
so if we have [4, -2, 2, -4] it would be sorted as [2, 2, 4, 4] so we can process doubles easily
but make sure to retain the negative value, once we encounter a number and its double, decrement their counts
if the count of every single key is 0, return true
0 is a special case, since it's it own double, so if 0 has an odd count, return false immediately
"""


from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq_map = {}

        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        sorted_keys = sorted(freq_map.keys(), key=abs) # sort by absolute value of only distinct keys

        if freq_map.get(0,0) % 2 != 0:
            return False

        freq_map[0] = 0

        for num in sorted_keys:
            count = freq_map[num]

            if count == 0:
                continue
            
            double = num * 2
            
            if freq_map.get(double, 0) < count:
                return False
            else:   # unecessary but clean for flow imo
                freq_map[num] = 0
                freq_map[double] -= count
        
        return True
            


            



        