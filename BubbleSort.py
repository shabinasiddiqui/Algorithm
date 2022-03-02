def BubbleSort(arr):
  
  n = len(arr)
  for i in range(n-1):
    swapped =False
    for j in range(0,n-1-i):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
        swapped = True
    if(swapped==False):
      break
  return arr

      

arr = [4,1,0,6,9,2,4]
BubbleSort(arr)
print("Sorted array: ")
for i in range(len(arr)):
  print(arr[i])