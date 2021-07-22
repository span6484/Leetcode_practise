class Solution:
    def combinationSum(self, candidates, target):

        temp = []
        record = []
        for i in candidates:
            temp = []
            if i <= target:
                temp.append(i)
                temp,record = self.find_val(temp, candidates, target,record)
            
        # print(record)
        return record
            
            
    def find_val(self, temp, candidates, target,record):
        # print(temp,candidates,target)
        if sum(temp) == target:
            a = sorted(list(temp))
            if a not in record:
                record.append(a)
            # print('recors:', record)
            return temp,record
        val = sum(temp)
        for i in candidates:
            if val + i <= target:
                temp.append(i)
                # print('if',record)
                temp,record = self.find_val(temp, candidates, target,record)
                # print(f'{temp} here')
                temp.pop()
                # print(f'{temp} here')
        return temp,record

a = Solution()
candidate = [2,3,6,7]
target = 7
record = a.combinationSum(candidate,target)
print(record)
