'''LEETCODE'''
'''209. Minimum Size Subarray Sum'''
from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    min_len = float("inf")
    win_sum = 0
    left = 0
    for right in range(n):
        win_sum += nums[right]
        while win_sum >= target:
            min_len = min(min_len,right-left+1)
            win_sum -= nums[left]
            left += 1
    return min_len if min_len != float("inf") else 0
nums = [2,3,1,2,4,3]
target = 7
print(minSubArrayLen(target, nums))

'''713. Subarray Product Less Than K'''
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    n = len(nums)
    prod = 1
    count = 0
    left = 0
    for right in range(n):
        prod *= nums[right]
        while prod >= k:
            prod /= nums[left]
            left += 1
        count += right - left + 1
    return count
nums = [10,5,2,6] 
k = 100
print(numSubarrayProductLessThanK(nums, k))

'''904. Fruit Into Baskets'''
def totalFruit(fruits: List[int]) -> int:
    n = len(fruits)
    max_len = 0
    left = 0
    fruit_count = {}
    for right in range(n):
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
fruits = [1,2,1]
print(totalFruit(fruits))