""" 
Given an integer array arr, and an integer target, 
return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

3 <= arr.length <= 3000 -> small

0 <= arr[i] <= 100 -> small

0 <= target <= 300 -> small

output -> large, need to return mod very large number

find the total number of 3-tuples that sum up to target
use res: int -> to keep track of result

use 2 pointers for this, just like regular 3sum

to use 2 pointers, need to make sure array is sorted

once you find a sum, there can be duplicates so all valid 3-tuples need to be accounted for

there are 2 or 3 cases depending on how you look at it

when you fix i, you're free to move the l and r pointers
so l + r must sum to target - i

case 1:
if arr[l] != arr[r], you have to find the number of duplicate elements between them

ex: [1, 2, 2, 3, 3] and target = 6, 
there are 2 2s and 2 3s, so even though (1, 2, 3) is valid, it needs to be counted 2 * 2 = 4 times

case 2:
if arr[l] == arr[r], that means all elements between them must be equal

ex: [1, 2, 2, 2, 2], target = 5,
there are 4 2s, and you have to choose 2 from the 4, so it's just 4C2 = 6.
also, once all these duplicates are accounted for, you can skip to the next itertion of the loop

case 3?:
if there are duplicate values for i, you DON'T skip them, they need to be counted

ex: [1, 1, 2, 2, 3, 3], target = 6, 
we don't skip past the 2nd 1 with i, we have to go through it as well

needed some help on this question ngl to consider all the cases
"""


from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        res = 0
        n = len(arr)


        arr.sort()

        for i in range(0, n - 2):
            l = i + 1
            r = n - 1

            desired = target - arr[i]

            while l < r:
                if arr[l] + arr[r] == desired:
                    
                    if arr[l] == arr[r]:
                        # everything between l and r is equal 
                        count = r - l + 1
                        res += count * (count - 1) // 2
                        break # everything has been considered, nothing left to check
                    else:
                        l_dup = 1
                        r_dup = 1

                        while arr[l + 1] == arr[l]:
                            l_dup += 1
                            l += 1
                        
                        while arr[r - 1] == arr[r]:
                            r_dup += 1
                            r -= 1
                        
                        res += (l_dup * r_dup)  # l and r are still on the last duplicate elements atp
                        l += 1
                        r -= 1
                
                elif arr[l] + arr[r] < desired:
                    l += 1
                
                else:
                    r -= 1

        return res % ((10 ** 9) + 7)
