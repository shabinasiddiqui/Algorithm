def mergeSort(arr):
  if len(arr)>1:
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    i=j=k=0

    while len(left)>i and len(right)>j:
      if left[i]<right[j]:
        arr[k]=left[i]
        i+=1 
      else:
        arr[k]=right[j]
        j+=1
      k+=1
    
    while i<len(left):
      arr[k]=left[i]
      i+=1
      k+=1
    
    while j< len(right):
      arr[k]=right[j]
      j+=1
      k+=1


def Print(arr):
  for i in range(len(arr)):
    print(arr[i],end=" ")

#main function
n = int(input("Enter the length of an array: "))
arr = []
print("Enter the elements in an array: ",end=" ")
for i in range(n):
  arr.append(int(input()))

print(f"Array before merge sort:{arr}")
mergeSort(arr)
print("\nArray after merge sort: ",end=" ")
Print(arr)


