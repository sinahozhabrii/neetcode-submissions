class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap.keys():
                hashmap[i] +=1
            else:
                hashmap[i]=1
        res = list(hashmap.items())

        res.sort(key=lambda x:x[1],reverse=True)
        res = res[:k]
        return [x[0] for x in res]