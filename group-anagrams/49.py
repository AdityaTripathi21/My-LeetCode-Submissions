"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

1 <= strs.length <= 10^4    -> small
0 <= strs[i].length <= 100  -> small
strs[i] consists of lowercase English letters.

goal -> group anagrams together, return a list of list of strings

how to group things together efficiently? -> maybe map
brute force approach, sort every single str into groups, so if you see a string, check if it can be sorted into one of the existing groups, if not, make a new group. 

observation: all anagrams when sorted are the same string
so we do need to sort every string we come across which is O(k log k) for sorting where k is the length of the string, and then n strings so that's O(n * k log k). Worst case let's assume every single word creates a separate group, so none of them are anagarams. this leads to n^2 checks and you compare each string so that's O(k) work, so in total that's O(n^2 * k) + O(n * k log k). This is brute force TC

observation: anagrams have the same character counts, so we can use a frequency map
for every single word, we first create a frequency map which is O(k) and for n words this is O(nk).
Afterwards, we can convert it to a tuple because tuples are immutable and we need immutable keys, so that's 
O(26) which is O(1). Afterwards, map lookups and appending is O(1), so the TC is O(nk). Using a 26 character map helps with SC because it's constant time. The flow is -> for every word, make frequency map, convert map into tuple, check if tuple already exists in outer map, if it does, append, otherwise, create new group."""



class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_map = defaultdict(list)   # type: ignore # map of tuple ints -> list of strings

        for word in strs:
            freq = [0] * 26

            for s in word:
                index = ord(s) - ord("a")
                freq[index] += 1

            key = tuple(freq)

            group_map[key].append(word)

        return list(group_map.values())
                