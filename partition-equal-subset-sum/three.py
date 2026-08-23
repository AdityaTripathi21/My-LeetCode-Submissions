class Solution:
    def canPartition(self, nums: List[int]) -> bool:    # type: ignore
        reachable = {0}
        total = sum(nums)
        target = total // 2

        if total % 2 == 1:
            return False

        for num in nums:
            for r in list(reachable):
                reachable.add(num + r)
                if num + r == target:
                    return True
        
        return False