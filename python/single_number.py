# Uses a set to detect pairs from a list, returns the single number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            if not numSet:
                numSet.add(num)
            else:
                numSet.discard(num) if num in numSet else numSet.add(num)
        return numSet.pop()
