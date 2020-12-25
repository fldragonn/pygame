# x ^ n 구현
#
# power(x, n): x의 n승을 구하는 함수 구현


def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)


# 2^10 = 1024
print(power(2, 10))
print(power(3, 3))
