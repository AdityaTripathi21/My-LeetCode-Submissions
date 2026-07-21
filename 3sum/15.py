class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:  # skip duplicates
                continue
            
            if n > 0:   # the loop is sorted, so if n is positive, every number after is positive
                break

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = n + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]: # skip duplicate left values
                        l += 1

                    # skipping left only is enough because right is dependent on left


        return res