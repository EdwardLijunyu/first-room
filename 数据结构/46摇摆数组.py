
#!/usr/bin/env Python
# coding=utf-8



nums=[1,5,9,1,5,6,7,5]


class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if len(nums) == 0:
            return 0

        pre = -1     #前一个位置的状态
        cur = 0      #当前位置的状态
        max_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  #升序状态置1
                cur = 1
            if nums[i] < nums[i - 1]:  #降序状态置1
                cur = 2
            if nums[i] == nums[i - 1]: #相等就跳过
                continue

            if cur != pre:   #当出现摆动时就+1
                max_len += 1
            pre = cur        #记录状态

        return max_len

S=Solution()
print(S.wiggleMaxLength(nums))