'''
 def merge_two_sorted(arr1,arr2):
    result=[]
    i = j = 0
    while i<len(arr1) and j< len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i +=1
        else:
            result.append(arr2[j])
            j +=1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
arr1=[1,3,5]
arr2=[2,4,6]
print(merge_two_sorted(arr1,arr2))
'''

def search_rotated_arr(arr,target):
    low=0
    high=len(arr)-1
    while low <= high:
        mid=(low+high)//2
        if arr[mid] == target:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low] <= target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<= target <=arr[high]:
                low= mid+1
            else:
                high=mid-1
    return -1
arr=[4,5,6,7,0,1,2]
target=6
print("Index:", search_rotated_arr(arr,target))
