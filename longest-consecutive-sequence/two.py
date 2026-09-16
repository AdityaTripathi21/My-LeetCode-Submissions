"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

0 <= nums.length <= 10^5 -> small/medium-ish
-109 <= nums[i] <= 10^9 -> large

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

the elements don't have to be in order -> so [1, 2, 3, 4]
elements also need to be consecutive, so I can't have something like 1, 2, 4, need a 3 in between to be valid or just 1,2

can also have duplicates like [1,0,1,2], so account for that, output is 3 not 4 because the 1 isn't counted twice

consecutive is the most important part, so if n exists, we need to know if n - 1 exists as well. 
so we need fast lookups, so we need a map most likely, don't know if this is correct approach tho

maybe check if every element can be the start of a sequence, so starting from 100, check if 101 exists
if not, then move on, once you go to 1, check if 2 is in list, since it is, then you continue checking and keep counting

however to do this, you need to go through the list already and create the map which for every element checks if the next element is in the list, acc wait there are no key value pairs, so instead we can use a set which still gives O(1) lookup. """


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set()
        best = 0

        for num in nums:
            num_set.add(num)

        for num in num_set:
            if num - 1 not in num_set:  # start of sequence
                curr = num
                count = 1

                while curr + 1 in num_set:
                    curr += 1
                    count += 1

                best = max(count, best)

        return best