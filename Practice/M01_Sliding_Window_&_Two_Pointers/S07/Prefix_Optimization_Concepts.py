'''1480. Running Sum of 1d Array'''
nums = [1,2,3,4]
res = [0] * len(nums)
for i in range(len(nums)):
    curr_sum = 0
    for j in range(0,i+1):
        curr_sum += nums[j]
    res[i] = curr_sum
print(res)
'''1732. Find the Highest Altitude'''
from typing import List
def largestAltitude(gain: List[int]) -> int:
    n = len(gain)
    alt = [0]*(n+1)
    for i in range(1,n+1):
        alt[i] = alt[i-1] + gain[i-1]
    return max(alt)
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))
#Optimsl soluion
def largestAltitude(gain: List[int]) -> int:
    max_altitude = 0
    current_altitude = 0
    for g in gain:
        current_altitude += g
        max_altitude = max(max_altitude, current_altitude)
    return max_altitude
gain1 = [-4,-3,-2,-1,4,3,2]
print(largestAltitude(gain1))
'''1991. Find the Middle Index in Array'''
def findMiddleIndex(self, nums: List[int]) -> int:
    total = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        right_sum = total - num - left_sum
        if left_sum == right_sum:
            return i
        left_sum += num

    return -1
nums = [2,3,-1,8,4]
print(findMiddleIndex(0, nums))
'''523. Continuous Subarray Sum'''