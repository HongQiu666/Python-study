s = '单引号来转也'
print(s)

a = "双引号也能转"

print(a)

san = """
    三引号，还能做啥？
    还可以吟诗作对呢
"""

print(san)

# 特殊的符号如何书写出？
s = "Les't go "
print(s)

b = 'Les\'t \n   go '

print(b)


# format 格式化（代替了以前的百分号）
def hq(p):
    print("你是:" + p)
    print("你是:{}".format(p))
    print("{},我在的噢，亲".format(p))
    print("我是大锤,你好啊,{0}".format(p))
    return None


p = "宏秋"
hq(p)

# 使用命名参数
ming = "我的钱包有{money}，{she}要跟我嗨！！！"
ren = ming.format(money="9999999", she="柳岩")
print(ren)


# 使用字典设置参数，需要解包
my = "I LOVE {she}"
my_dict = {"she": "柳岩"}
my2 = my.format(**my_dict)
print(my2)

me = "I LOVE {she} so mach"
me2 = me.format(**my_dict)
print(me2)