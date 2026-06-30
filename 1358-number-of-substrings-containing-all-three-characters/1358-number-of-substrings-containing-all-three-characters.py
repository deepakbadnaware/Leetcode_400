class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0, 0, 0]
        left = 0
        result = 0
        
        for right in range(len(s)):
            count[ord(s[right]) - ord('a')] += 1
            
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                count[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            result += left
        
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna