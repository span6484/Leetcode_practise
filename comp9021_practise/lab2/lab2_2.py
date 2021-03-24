import sys

def check(val):
    lst = []
    end = val//2
    for i in range(1,end+1):
        if (val % i == 0):
            if i not in lst and i != val:
                lst.append(i)
    
    # check perfect
    sum = 0
    # print(f'list is {lst}')
    for i in lst:
        sum += i

    if sum == val:
        return True
    else:

        return False
    

a = input("Input an integer: ")


val = int(a)

for i in range(2,val+1):
    perfect_val_judge = check(i)
    # print(f"{i} : {perfect_val_judge}")
    if perfect_val_judge:
        print(f"{i} is a perfect mumber")



