class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: O(N * 2^N)
        #   - There are 2^N possible subsets.
        #   - For each subset we iterate over N bits to build the subset list.
        # Space Complexity: O(2^N) for the output list (excluding recursion stack).
        #   - The algorithm uses O(1) extra space besides the result container.
        # This bit‑mask approach is optimal for generating all subsets, as any solution must
        # output 2^N subsets.
        # The code is correct and does not need changes. A minor Pythonic tweak could be:
        #   ans = [ [nums[j] for j in range(n) if (i >> j) & 1] for i in range(1 << n) ]
        # but the current explicit loops are clear and fine.
        n=len(nums)
        total_subset=1<<n
        ans=[]
        for i in range(total_subset):
                lst=[]
                for num in range(n):
                    if i &(1<<num) !=0:
                        lst.append(nums[num])
                ans.append(lst)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna