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

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = create_dict(p)
        p_len = len(p)
        arr_save = []
        if len(s) < p_len:
            return arr_save
        #print("p dict:" + str(target))
        for i in range(len(s)):
            count = 0
            arr = create_dict(s[i:p_len+i])
           # print("arr dict:" + str(arr))    
            for j in s[i:p_len+i]:
                if arr.get(j) == None or target.get(j) == None:
                    continue
                if arr[j] == target[j] :
                    count = count + 1
                 #   print("count is "+ str(count))
                if count == p_len:
                    arr_save.append(i)
        return arr_save