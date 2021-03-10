# coding:utf-8
# 任意进制转换
def toStr(n,base):
    converString = "0123456789ABCEDF"
    if n < base:
        return converString[n]
    
    else:
        return toStr(n//base, base) + converString[n%base]


print(toStr(9,2))