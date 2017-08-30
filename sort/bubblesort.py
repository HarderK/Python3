def bubblesort(li):
    length = len(li)
    temp = None, flag = 1
    i = 1
    while i < length and flag == 1:
        flag = 0
        for j in range(length - i):
            if li[j] > li[j+1]:
                temp = li[j+1]
                li[j+1] = li[j]
                li[j] = temp
                flag = 1
    return li


