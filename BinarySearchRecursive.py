def BinarySearch(arr,low,high,key):
  if low<=high:

    mid = (low+high)//2
    if arr[mid]== key:
      return mid
    elif arr[mid]<key:
      return BinarySearch(arr,mid+1,high,key)
    else:
      return BinarySearch(arr,low,mid-1,key)
  else:
    return -1
  
  #main function
arr = [1,2,4,6,8,9,12,14,21,43]
k = int(input("Enter key element: "))
result =BinarySearch(arr,0,len(arr)-1,k)
if result!=-1:
  print(f"Key element {k} is found at location {result}")
else:
  print(f"Element not found")

