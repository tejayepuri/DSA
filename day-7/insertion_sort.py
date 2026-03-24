
'''
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1]=key


arr=[5,3,4,1]
insertion_sort(arr)
print(arr)
'''

'''
def insertion_sorted(arr, element):
    arr.append(0)
    i=len(arr) - 2

    while i>=0 and arr[i]> element:
        arr[i+1]=arr[i]
        i-=1


        arr[i+1]=element
arr=[2,4,6,8]
insertion_sorted(arr,5)
print(arr)
'''

def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot=arr[0]
    left=[x for x in arr[1:]if x<=pivot]
    right=[x for x in arr[1:]if x>=pivot]


    return quick_sort(left) + [pivot] + quick_sort(right)

arr=[5,3,8,4,2]
print(quick_sort(arr))
