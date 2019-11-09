

# 位置参数(没传够对应的位置的参数，是会报错)
def wei(li,
        zhu,
        he):
    print("1" + li)
    return None


wei("12", 2, 3)


# 默认参数（主要在函数定义的时候固定默认值;有默认参数的变量，可以不用给对应的值）
def gu(aa, bb, cc=10):
    print(aa + cc)


gu(1, 2)


# 关键字参数（传入的时候带关键字给固定的值）
def jian(e, b, f):
    print(e + f)


jian(b=1, e=2, f=3)
