def merge(nums, start, mid, end):

    left = nums[start:mid].copy()
    right = nums[mid:end].copy()
    new_array = []
    time_left = len(left)
    time_right = len(right)
    index_left = 0
    index_right = 0
    while index_left < time_left and index_right < time_right:
        if left[index_left] < right[index_right]:
            new_array.append(left[index_left])
            index_left += 1
        else:
            new_array.append(right[index_right])
            index_right += 1
    while index_left < time_left:
        new_array.append(left[index_left])
        index_left += 1
    while index_right < time_right:
        new_array.append(right[index_right])
        index_right += 1
    nums[start:end] = new_array
    return

def mergeSort(nums, start, end):
    print('-----------------------')
    for i in nums:
        print(i)
    print('---------------------')
    mid = (start + end) // 2

    #for two arrays [3,-1] 
    if (end - start <= 1):
        end = end+1
        mid = (start + end) // 2
        merge(nums,start,mid,end)
        return nums
    print(f"sort1  : start:{start}   end:{mid}")
    #sort1
    if len(nums[start:mid]) != 1:
        mergeSort(nums, start,mid)

    print(f"sort2  : start:{mid}   end:{end}")

    #避免取不到最后一个数
    if end == len(nums) - 1:
        end = end + 1               
        print("now end is ",end)
    #sort2       
    if len(nums[mid:end]) != 1:
        mergeSort(nums,mid, end)
    
    
    #merge3
    print(f"merge3  : start:{start}   mid: {mid} end:{end}")

    print(f"before merge {nums[start:end]}")
    merge(nums,start, mid, end)
    print(f"----------------------start: {start}  mid:{mid} end: {end}")
    print(f"after merge {nums[start:end]}")
    nums = nums[start:end+1]
    return nums
nums = [3,-1]
left = 0
right = len(nums)-1
index_record = []
nums = mergeSort(nums, left, right)
print(nums)


##solution
class Solution:
    def sortArray(self, nums):
        # merge function
        # merge
        def merge(nums, start, mid, end):
            left = nums[start:mid].copy()
            right = nums[mid:end].copy()
            new_array = []
            time_left = len(left)
            time_right = len(right)
            index_left = 0
            index_right = 0
            while index_left < time_left and index_right < time_right:
                if left[index_left] < right[index_right]:
                    new_array.append(left[index_left])
                    index_left += 1
                else:
                    new_array.append(right[index_right])
                    index_right += 1
            while index_left < time_left:
                new_array.append(left[index_left])
                index_left += 1
            while index_right < time_right:
                new_array.append(right[index_right])
                index_right += 1
            nums[start:end] = new_array
            return

        def mergeSort(nums, start, end):
            if (end - start <= 1):
                end = end+1
                mid = (start + end) // 2
                merge(nums,start,mid,end)
                return nums
            mid = (start + end) // 2
            #sort1
            if len(nums[start:mid]) != 1:
                mergeSort(nums, start,mid)
            #sort2
            if end == len(nums) - 1:
                end = end + 1
            if len(nums[mid:end]) != 1:
                mergeSort(nums,mid, end)

            #merge3
            merge(nums,start, mid, end)
            nums = nums[start:end+1]
            return nums
        
        
        if len(nums) == 1:
            return nums
        elif len(nums) == 0:
            return None
        else:
            nums = mergeSort(nums, 0, len(nums)-1)
            return nums



#solution2:

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(nums, left, mid, right):
            array_A = nums[left:mid].copy()
            array_B = nums[mid:right].copy()
            array_C = []
            while array_A != [] and array_B != []:
                if array_A[0] <= array_B[0]:
                    array_C.append(array_A.pop(0))
                else:
                    array_C.append(array_B.pop(0))
            while array_A != []:
                array_C.append(array_A.pop(0))
            
            while array_B != []:
                array_C.append(array_B.pop(0))
            nums[left:right] = array_C
            return nums
        
        def divide(nums, left, right):
            mid = (left+right)//2

            if len(nums[left:mid]) > 1:
                divide(nums, left, mid)
            if len(nums[mid:right]) > 1:
                divide(nums, mid, right)
                
            nums = merge(nums, left, mid, right)
            return nums
        left = 0
        right = len(nums)
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums
        else:
            nums = divide(nums, left, right)
        
        return nums