class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)

        print(count)
        for char in ransomNote:
            if char not in count:
                return False

            elif count.get(char) <= 0:
                return False
            
            else:
                count[char] -= 1

        return True


        