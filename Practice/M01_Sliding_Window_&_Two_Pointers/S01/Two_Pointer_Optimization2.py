'''Remove Duplicates from Sorted Array(LeetCode-26)'''
'''
from typing import List
def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    k = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]

    return k + 1

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
'''

'''Remove Elemet(LEETCODE-27)'''

'''
from typing import List
def removeElement(self, nums: List[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
val = 5 
nums = [1,2,3,4,5,6,7,8]
print(removeElement(nums,val))
'''


'''167. Two Sum II - Input Array Is Sorted'''
'''
from typing import List
def twoSum(numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1,right+1]
            elif s > target:
                right -= 1 
            else:
                left += 1 
numbers = [2,7,11,15]
target = 9 
print(twoSum(numbers,target))
'''
