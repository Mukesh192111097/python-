def minMax(arr):


    min_value = 0

    max_value = 0

    n=len(arr)

    arr.sort()

    j=n-1

    for i in range(n-1):

        min_value += arr[i]

     
        max_value += arr[j]

        j-=1


    print(min_value," ",max_value)


arr=[10, 9, 8, 7, 6, 5]

arr1=[100, 200, 300, 400, 500]
 
minMax(arr)
minMax(arr1)
 
