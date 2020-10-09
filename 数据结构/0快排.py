def exchange(arr,low,high):
    tmp=arr[low]


    while low<high:
        while low<high and arr[high]>=tmp:  #满足右边的数大于tmp时，就移动右边的指针，直到右边出现小于tmp的数，退出循环
            high-=1
        arr[low]=arr[high] #就把右边小于tmp的数给到左边的空位

        while low<high and arr[low]<=tmp:  #满足左边的数小于tmp时，就移动左边的指针，直到左边出现大于tmp的数，退出循环
            low+=1
        arr[high]=arr[low] #就把左边大于tmp的数给到右边的空位

    arr[low]=tmp

    return low


def quickorder(arr,low,high):
    if low<high:

        point=exchange(arr,low,high)

        quickorder(arr,low,point-1)
        quickorder(arr,point+1,high)


arr=[2,9,5,7,3,1,6,4]

quickorder(arr,0,7)
print(arr)