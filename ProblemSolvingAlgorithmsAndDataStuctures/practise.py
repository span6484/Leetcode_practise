class Solution(object):
    def permuteUnique(self, nums):
        
        res = []
        
        self.findResult(nums, [], res, len(nums))
        
        return res
    
    def findResult(self,nums, partial, res, lenNums):
        
        if lenNums == 0:
            res.append(list(partial))
        else:
            
            for i in range(len(nums)):
                
                if i not in partial:
                    partial.append(i)
                    self.findResult(nums, partial, res,lenNums-1)
                    partial.pop()

if __name__ == "__main__":
    nums = [1,2,3]
    a = Solution().permuteUnique(nums)

    print(a)