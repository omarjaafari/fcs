def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
        while arr[j -1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -=1
arr = [2,3,4,5,1,0]
insertion_sort(arr)
print(arr)

# First it will start with second item from the list because the for loop start from index 1
# Then it will make a var called j which is same as i
# While j-1 index which is 0 in the first time is greate then the j which is 1 in the first time and j is greater than 0
# If the while loop is true then swap the index of j-1 and j to be j and j-1
# then make j -1  so we can stop the while loop
# 2 < 4 --> don't swap
# j = 0 --> stop
# 4 > 3 --> swap
# j = 1 --> don't stop
# 2 < 3 --> don't swap
# j = 0 --> stop
