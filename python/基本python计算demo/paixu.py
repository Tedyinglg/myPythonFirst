li = [11, 1, 2, 5, 3, 10, 6, -2, 0, -5, 18]
def paixu():
    for i in range(len(li)):
        j = i
        min = li[i]
        while j < len(li):    
            if(min > li[j]):
                temp = min
                min = li[j]
                li[j] = temp
            j += 1
        li[i] = min

    print(li)

def paixu2():
    for i in range(len(li)):
        j = i+1
        while j < len(li):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
            j += 1
    print(li)
paixu2()

