class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        ans = [0] * n
        pos_i, neg_i = 0, 1          
        for x in nums:
            if x > 0:
                ans[pos_i] = x
                pos_i += 2
            else:
                ans[neg_i] = x
                neg_i += 2
        return ans
