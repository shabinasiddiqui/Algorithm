def selectionSort(arr):
  for i in range(len(arr)):
    min = i
    for j in range(i+1,len(arr)):
      if arr[min]>arr[j]:
        min = j
    arr[i],arr[min] =arr[min],arr[i]

      
#main function
n = int(input("Enter the length of an array: "))
print("Enter elements in an array: ")
arr =[]
for i in range(n):
  arr.append(int(input()))
  
print("Original array: ",arr)

selectionSort(arr)
print("Array after selection sort: ")
print(arr)

