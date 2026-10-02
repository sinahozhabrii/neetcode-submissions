class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            diff=target-n
            index_diff = hashmap.get(diff,None)
            if index_diff is not None:
                return [index_diff,i]
            hashmap[n]=i