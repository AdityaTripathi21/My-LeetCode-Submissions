"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. 

Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

1 <= time.length <= 6 * 10^4 -> kind of big
1 <= time[i] <= 500 -> small

i < j with (time[i] + time[j]) % 60 == 0 -> important

songs with the same number of seconds are not counted as duplicates

when you get to time[i], check if 60 - time[i] % 60 is in the list, 
so for example 60 - 20 % 60 = 40 % 60 = 40, so you use a map
and check to see what numbers % 60 is equal to that, so for example
40 and 100 would show up, because 40 % 60 = 40, 100 % 60 = 40, 
so the map would be key = 40, value = 2, because there are 2 values at that
to be more general, key -> that number % 60
lets say we had 80, so then 60 - 80 = -20, so then we -20 mod 60 is 40, so it works for negatives as well
"""


from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod_map = {}
        res = 0

        for t in time:
            needed = (60 - t) % 60
            if needed in mod_map:
                res += mod_map[needed]
            key = t % 60
            mod_map[key] = mod_map.get(key, 0) + 1

        return res 