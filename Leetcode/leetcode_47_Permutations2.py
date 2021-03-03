# -*- coding:utf8 -*-
#想法： 先存入index， 然后翻译成对应array，稍后筛选
class Solution(object):
    def permute(self, nums):

        if len(nums) == 0:
            return nums

        if len(nums) == 1:
            return [nums]

        nums = sorted(nums)
        res = []
        partial = []

        res1 = []
        partial1 = []
        self.getResult(partial, nums, len(nums), res)
        for i in res:
            for j in i:
                partial1.append(nums[j])
            res1.append(partial1)
            partial1 = []

        partial2 = []
        for i in res1:
            if i not in partial2:
                partial2.append(i)
        return partial2


    # partial: 临时存储的list， 存满一个弹出一次，rem is the len(nums)
    def getResult(self,partial, nums, rem, result):
        print("partial is %s" % partial)
        if rem == 0:
            result.append(list(partial))
            print("result is %s" % result)
        
        else:

            for i in range(len(nums)):
                print("n is %d" % i)    
                if i not in partial:
                    partial.append(i)
                    self.getResult(partial, nums,rem-1,result)
                    print("time")
                    partial.pop()
                    print(partial)

        
        




if __name__ == "__main__":
    nums = [1,2,1]
    a = Solution().permute(nums)

    print(a)