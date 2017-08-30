def quicksort(li, low=0, high=-1):
    i = low
    high = high if high > 0 else len(li) + high
    j = high
    temp = li[low]
    while i < j:
        while i < j and li[j]  > temp:
            j -= 1
        if i < j:
            li[i] = li[j]
            i += 1
        while i < j and li[i] < temp:
            i += 1
        if i < j:
            li[j] = li[i]
    li[i] = temp
    print(li)
    if low < i-1: quicksort(li, low, i-1)
    if j+1 < high: quicksort(li, j+1, high)


