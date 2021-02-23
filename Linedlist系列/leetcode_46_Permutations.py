# -*- coding:utf8 -*-
# list ‘=’ 只是指向，比如‘num = nums’只是将num指向nums， 要是想单纯的复制值，建议使用 copy 或者 num = list（nums）
class Solution(object):
    def permute(self, nums):

        if len(nums) == 0:
            return nums

        if len(nums) == 1:
            return [nums]

        nums = sorted(nums)
        res = []
        partial = []
        self.getResult(partial, nums, len(nums), res)
        return res


    # partial: 临时存储的list， 存满一个弹出一次，rem is the len(nums)
    def getResult(self,partial, nums, rem, result):

        if rem == 0:
            result.append(list(partial))
        
        else:

            for n in nums:
                if n not in partial:
                    partial.append(n)
                    self.getResult(partial, nums,rem-1,result)
                    partial.pop()

        
        




if __name__ == "__main__":
    nums = [1,2,3]
    a = Solution().permute(nums)

    print(a)