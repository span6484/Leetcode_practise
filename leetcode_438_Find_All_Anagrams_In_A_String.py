def create_dict(str):
    arr = dict()
    num = 1
    for i in str:
        arr[i] = 0
    for i in str:
        if arr[i] != 0:
            num = arr[i] + 1
        arr[i] = num
        num = 1
    return arr


def findAnagrams(s: str, p: str):
    target = create_dict(p)
    p_len = len(p)
    arr_save = []
    arr_index = []
    arr_return = []
    index = 0
    if len(s) < p_len:
        return arr_save
    #print("p dict:" + str(target))
    for i in range(len(s)):
        arr = create_dict(s[i:p_len+i])
        arr_save.append(arr)
        arr_index.append(i)
    print(arr_index)

    for i in range(len(arr_save)):
        if arr_save[i] == target:
            arr_return.append(index)
        index = index + 1
    return arr_return


s = 'abac'
p = 'ab'
arr = findAnagrams(s, p)
print(arr)
