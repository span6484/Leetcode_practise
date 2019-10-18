# use normal, erro is overtime
def findAnagrams(s:str, p: str):
    if len(s) <= 20100 and len(p) <= 20100:
        p = sorted(p)
        arr = []
        for i in range(len(s)):
            print ('i is ' + str(i))
            print('len is ' + str(len(s) - 1))
            if p == sorted(s[i:len(p)+i]):
                print('p is ' +str(p))
                print('s is '+ str(sorted(p[i:len(p)+i])))
                arr.append(i)
                print(arr)
        return arr


# s = "aba"
# p = "a"
# arr = findAnagrams(s,p)
# print(arr)