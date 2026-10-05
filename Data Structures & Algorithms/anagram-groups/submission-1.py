class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for i in strs:
            if tuple(sorted(i)) in res.keys():
                res[tuple(sorted(i))].append(i)
            else:
                res[tuple(sorted(i))] = [i]
        return list(res.values())
            