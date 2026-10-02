class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        j=None
        for i in nums:
            if i==j:
                return True
            j = i
        return False