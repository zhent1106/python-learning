"""
两种方法实现斐波那契数列
@Date 2020.05.04
"""

# 普通方式实现斐波那契数列
def fibonacci(n):
    if n <= 1:
        return [1]
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    return fib

# 使用生成器方式实现斐波那契数列
def fibonaccil(n):
    a, b = 1, 1
    for _ in range(n):
        # 遇到yield返回，下次再进入函数体时，从yield的下一句开始执行
        yield a
        a, b = b, a+b

if __name__=='__main__':
    print(fibonacci(5))
    print(list(fibonaccil(5)))