# recursive call
#
# recursive01.py

# 재귀함수


def hello(cnt):
    # 재귀 종료 조건
    if cnt == 0:
        return

    print('hello, recursive!', cnt)
    cnt = cnt - 1
    hello(cnt)


hello(3)
