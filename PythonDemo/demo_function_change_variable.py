def change2(l1):
    l1[2] = 10086

def change1(l1):
    l1 = [4,5,6]

def main():
    l1 = [1,2,3]
    change1(l1)
    print("after change1: ", l1)
    # 输出: after change1:  [1, 2, 3]
    # NOTE:调用函数, 不能再函数里改变外面穿进去的变量的指向

    l1 = [1,2,3]
    change2(l1)
    print("after change2: ", l1)
    # 输出: after change2:  [1, 2, 10086]
    # NOTE: 调用函数,可以改变外面传进来的变量所指向的容器里面的值

if __name__ == "__main__":
    main()


