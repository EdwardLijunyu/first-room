'''

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。


'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if (len(nums1)+len(nums2))==0:
            return 0
        #用两个列表序号指针指向两个列表
        #依次从小到达搜寻到n/2位置
        #如果是奇数，就返回中间位置的数 mid2
        #如果是偶数就返回中间位置的数加上前一个位置的数除以2：（mid1+mid2）/2
        s1=0
        s2=0
        mid1=0
        mid2=0

        for _ in range((len(nums1)+len(nums2))//2+1):
            if s1>len(nums1):#指针超出列表范围,就只在另一个列表上循环
                mid1=mid2
                mid2=nums2[s2]
                s2+=1
                continue
            if s2>len(nums2):
                mid1=mid2
                mid2=nums1[s1]
                s1+=1
                continue
            if nums2[s2]>nums1[s1]:#指针没有超出，就找到较小的元素进行循环
                mid1=mid2
                mid2=nums1[s1]
                s1+=1
            else:
                mid1 = mid2
                mid2 = nums2[s2]
                s2 += 1

        if (len(nums1)+len(nums2))%2==0:#偶数个元素
            return (mid1+mid2)/2.0
        else:
            return mid2 #奇数个元素

