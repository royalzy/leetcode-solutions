class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''treat every char/gap as centers of palindrome'''
        if not s:
            return 0

        longest = ""

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    if len(longest) < (r-l-1):
                        longest = s[l+1:r]
                    
                else: 
                    break

            l, r = i, i+ 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    if len(longest) < (r-l-1):
                        longest = s[l+1:r]
                    
                else: 
                    break

        return longest

            
