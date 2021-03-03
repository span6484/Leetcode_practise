class Solution:
    def reverse(self, x: int) -> int:
        
        if(x>2**31-1 or x<-2**31):
            return 0
        
        if(x<0):
            sign = True
            x = -1 * x
        else:
            sign = False
            
        arr = []    
        a = str(x)
        strlen = len(a)
        
        index = strlen - 1
        
        while index != -1:
            arr.append(x//10**index)
            x = x - x//10**index * 10**index
            index -= 1
            
        new_value = 0
        for i in range(0, strlen):
            new_value += arr[i] * 10**i
        
        if (sign == True):
            new_value = -1*new_value
        
        if(new_value>2**31-1 or new_value<-2**31):
            return 0
        return new_value
        