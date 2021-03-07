# -*- coding:utf8 -*-
#想法： 先存入index， 然后翻译成对应array，稍后筛选
class Solution(object):
    def permuteUnique(self, nums):

        result = []
        partial = []
        
        filer_result = []
        
        self.findResult(nums, partial, result)
        
        self.filer(nums,result, filer_result)
        return filer_result
    
    def findResult(self, nums, partial, result):
        
        if len(partial) == len(nums):
            result.append(list(partial))
        
        for i in range(len(nums)):
            if i not in partial:
                partial.append(i)
                self.findResult(nums, partial, result)
                partial.pop()
    
    def filer(self, nums,result, filer_result):
        
        
        for i in result:
            partial1 = []
            for j in i:
                partial1.append(nums[j])
            
            if partial1 not in filer_result:
                filer_result.append(partial1)

        
        

class Solution2(object):
    def permuteUnique(self, nums):
        
        self.ret = []
        self.used = [False] * len(nums)
        nums = sorted(nums)
        self.backtrack(nums = nums, partial = [])
        return self.ret
    
    def backtrack(self, nums, partial):
        if len(partial) == len(nums):
            self.ret.append(partial[:])
        
        else:
            for i, num in enumerate(nums):
                if not self.used[i]:
                    if i == 0 or nums[i-1] != nums[i] or self.used[i-1]:
                        partial.append(nums[i])
                        self.used[i] = True
                        self.backtrack(nums, partial)
                        partial.pop()
                        self.used[i] = False


if __name__ == "__main__":
    nums = [1,2,1]
    a = Solution2().permuteUnique(nums)

    print(a)