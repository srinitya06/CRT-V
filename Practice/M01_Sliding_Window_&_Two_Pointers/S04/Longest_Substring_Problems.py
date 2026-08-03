'''LEETCODE 
3: Longest Substring Without Repeating Characters
'''
def lengthOfLongestSubstring(s: str) -> int:
    left, ans = 0, 0
    seen = set()
    
    for right in range(len(s)):
        # Indent everything inside the for loop
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
            
        seen.add(s[right])
        ans = max(ans, right - left + 1)
        
    return ans
s = "abcabcbb"
print(lengthOfLongestSubstring(s)) 
