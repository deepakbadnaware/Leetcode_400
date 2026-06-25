class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            count = 0
            for j in nums:
                if (j >> i) & 1:      # is bit b set in n?
                    count += 1
            if count % 3 != 0:
                result |= (1 << i)   # set bit b in result
        if result >= 2**31:
            result -= 2**32
        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna