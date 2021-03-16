def test(lst,final):
    partial = []
    for i in lst:
        partial.append(i)
        final.append(list(partial))
    return final



def add(a, val):
    a += val
    return a
a = 8

a = add(a,8)

print(a)


b = [1,2,3]
def add2(b,val):
    b *= 2
    return b

add2(b,2)

print(b)