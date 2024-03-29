
'''
输入一个整数，输出该数的二进制表示中的1的个数，其中负数用补码表示

请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，
把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        n = 0xFFFFFFFF & n  # 将负数
        print(bin(n))  #bin()是将数转化为二进制，负数转化为补码 int有32位 4个字节，一个字节8位

        k = 0
        for i in str(bin(n)):
            if i == "1":
                k += 1

        return k

test=Solution()

print(test.hammingWeight(-6))

'''
反码的表示方法是:
    正数的反码是其本身
    负数的反码是在其原码的基础上, 符号位不变，其余各个位取反.

补码的表示方法是:
    正数的补码就是其本身
    负数的补码是在其原码的基础上, 符号位不变, 其余各位取反, 最后+1. (即在反码的基础上+1)
    
    
只有将负数转化为补码才能进行正确的加法运算1+（-1）=0
'''











