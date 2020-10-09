
def fib_Recursive(n):
    #斐波那契数 递归方法，
    # 形成的序列称为斐波那契数列。该数列由 0 和 1 开始，
    # 后面的每一项数字都是前面两项数字的和。
    if n<0:
        return None
    if n==0:
        return 0
    if n==1:
        return 1
    if n >1:
        y=fib_Recursive(n-1)+fib_Recursive(n-2)
    return y



def fib(n):
    #斐波那契数，
    # 形成的序列称为斐波那契数列。该数列由 0 和 1 开始，
    # 后面的每一项数字都是前面两项数字的和。
    if n<0:
        return None
    if n==0:
        return 0
    if n==1:
        return 1
    if n >1:
        a=0
        b=1
        for i in range(n-1):
            y=a+b
            a=b
            b=y
        return y

n=6
print("递归：",fib_Recursive(n))
print("循环：",fib(n))





















