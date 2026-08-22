class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size = len(needle)
        if len(haystack) < size:
            return -1
        
        for i in range(len(haystack) - size + 1):
            check = haystack[i:i + size]
            if check == needle:
                return i
            
        return -1
            