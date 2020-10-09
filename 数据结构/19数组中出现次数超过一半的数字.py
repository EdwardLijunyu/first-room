class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        #新建一个字典，出现的元素为key，出现的次数为value
        dict={}
        len_nums=len(nums)

        for num in nums:
            if num in dict: #如果这个元素已经出现过，那么就将value+1
                dict[num]+=1
            else:
                dict[num]=1 #没有出现过就存下
            if dict[num]>(len_nums>>1):
                return num

        return 0