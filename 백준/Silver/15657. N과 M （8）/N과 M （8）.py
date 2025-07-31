import sys
input = sys.stdin.readline

n, m = map(int, input().split())
list1 = sorted(list(map(int, input().split())))

array = []

def back():
    if len(array) == m:
        print(*array)
        return
    
    for i in list1:
        if array:
            if array[-1] <= i:
                array.append(i)
                back()
                array.pop()

        else:
            array.append(i)
            back()
            array.pop()

back()