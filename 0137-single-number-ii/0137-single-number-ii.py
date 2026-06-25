class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen={}
        for i in nums:
            seen[i]=seen.get(i,0)+1
        
        for num in seen:
            if seen[num]==1:
                return num
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna