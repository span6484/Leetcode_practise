def func(x, y):
    x += 100
    y += 100
    return x, y



def main():
    a = 1
    b = 2
    print("before add:",a,b)
    a, b = func(a, b)
    print("after add:",a,b)

# 输出:
# before add: 1 2
# after add: 101 102

if __name__ == "__main__":
    main()

