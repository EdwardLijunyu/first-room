
'''

我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

'''



# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         if n < 1:
#             return None
#
#         def isUglynumber(num):
#
#             while num % 2==0:
#                 num=num/2
#             while num % 3==0:
#                 num=num/3
#             while num % 5 == 0:
#                 num = num / 5
#
#             if num==1:
#                 return True
#             else:
#                 return False
#
#         count=n
#         i=1
#         while True:
#             if isUglynumber(i):
#                 count-=1
#             if count==0:
#                 return i
#             else:
#                 i+=1
#
#
# s=Solution()
#
# out=s.nthUglyNumber(2000)
# print(out)

#以上方法比较慢

#改用动态规划的思想
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        if n<1:
            return 0
        uglylist=[1]
        twopointer,threepointer,fivepointer=0,0,0

        count=1

        while count!=n:
            minValue=min(2*uglylist[twopointer],3*uglylist[threepointer],5*uglylist[fivepointer])

            uglylist.append(minValue)

            if minValue==2*uglylist[twopointer]:
                twopointer+=1
            if minValue==3*uglylist[threepointer]:
                threepointer+=1
            if minValue==5*uglylist[fivepointer]:
                fivepointer+=1

            count+=1

        return uglylist[-1]


s=Solution()
for i in range(1,20):
    out=s.nthUglyNumber(i)
    print(out)


