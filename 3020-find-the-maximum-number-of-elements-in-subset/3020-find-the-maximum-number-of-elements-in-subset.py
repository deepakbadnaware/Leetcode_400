class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 1  # a single element is always a valid subset (m = 1)

        # 1 squares to itself, so just use as many 1's as possible (length must be odd)
        if 1 in count:
            ones = count[1]
            if ones % 2 == 0:
                ones -= 1
            ans = max(ans, ones)

        for x in count:
            if x == 1:
                continue
            length = 1
            cur = x
            while count[cur] >= 2:
                nxt = cur * cur
                if nxt in count:
                    length += 2
                    cur = nxt
                else:
                    break
            ans = max(ans, length)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna