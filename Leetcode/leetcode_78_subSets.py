class Solution(object):
    def subset(self, nums):
        partila = []
        self.result = []
        
        self.backTrack(nums, partila, 0)
        
        return self.result

    def backTrack(self, nums, partial, start):
        self.result.append(list(partial))
        print("----------------")
        for i in range(start, len(nums)):
            partial.append(nums[i])
            print(i)
            self.backTrack(nums, partial, i+1)
            print("before pop: %s"%partial)
            partial.pop()
            print("after pop: %s"%partial)



if __name__ == "__main__":
    num = [1,2,3]
    a = Solution().subset(num)
    print(a)
