from statistics import LinearRegression


def LinearSearch(arr,key):
  for i in range(len(arr)):
    if arr[i]==key:
      return i
  return -1

  #main function

arr =[4,6,7,0,3,2,1,65,32,21]
k = int(input("Enter key element: "))
if LinearSearch(arr,k)!=-1:
  print(f"The key element {k} is present at location {LinearSearch(arr,k)} ")
else:
  print(f"The key element {k} is not present in the given array")

