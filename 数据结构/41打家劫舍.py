class Solution:
    def rob(self, nums) -> int:
        if nums == []:
            return 0
        if len(nums) < 2:
            return nums[0]

        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]

        if dp[0] < nums[1]:  # 用dp[i]表示0到i个房间中的最大抢劫金额
            dp[1] = nums[1]
        else:
            dp[1] = dp[0]

        for i in range(2, len(nums)):
            if dp[i - 1] == dp[i - 2]:  # 前一位没有选。直接选当前位加
                dp[i] = dp[i - 1] + nums[i]
            else:  # 前一位选了，比较当前位i家i-2位和i-1位谁大
                if nums[i] + dp[i - 2] > dp[i - 1]:  # 如果 [i]+[i-2]大，就dp[i]=当前位金额加上前i-2的金额
                    dp[i] = dp[i - 2] + nums[i]
                else:
                    dp[i] = dp[i - 1]  # 否则就不取当前位金额，dp[i]=dp[i-1]一样

        return dp[len(nums) - 1]