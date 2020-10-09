def rob(nums) -> int:
    dp = [0 for i in range(len(nums))]

    dp[0] = nums[0]
    dp[1] = nums[1] if dp[0] < nums[1] else 0

    for i in range(2, len(nums)):
        if dp[i - 1] == 0:
            dp[i] = nums[i]
        else:
            if nums[i] > dp[i - 1]:
                dp[i - 1] = 0
                dp[i] = nums[i]

    return sum(dp)

h1=[2,7,9,3,1]
print(rob(h1))