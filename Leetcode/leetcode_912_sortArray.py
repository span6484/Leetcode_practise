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