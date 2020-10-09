'''

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        length = len(s)
        dp = [[False for i in range(length)] for i in range(length)]  # 动态方程初始化

        for i in range(length):  # 动态方程 只要一个元素一定是True
            dp[i][i] = True

        max_line = 1
        max_start = 0
        for j in range(1, length):  # dp[i][j]表示第i个到j这一段的字符串是否是回文
            for i in range(j):
                if s[i] == s[j]:  # 第i和第j个字符相等，如果i到j小于3那么一定是回文，让dp为True，如果大于3，就等于中间的字符是否是回文
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and max_line < j - i + 1:  # 当出现更长的回文，就更新最长，和该回文起始位置
                    max_line = j - i + 1
                    max_start = i

        return s[max_start:max_line + max_start]
