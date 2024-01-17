class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numDict = {}
        for num in arr:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        return len(numDict.values()) == len(set(numDict.values()))
