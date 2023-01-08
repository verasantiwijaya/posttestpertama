def partition(arr, low, high):
   pivot = arr[low]
   i = low+1
   j = high
   while True :
    while i <=j and arr[i] <= pivot:
        i = i+1
    while i <=j and arr[j] > pivot:
        j = j-1
    if i <= j:
        arr[i], arr[j] = arr[j], arr[i]
    else:
        break
   arr[low], arr[j] = arr[j], arr[low]
   return j

def quicksort(arr, low, high):
    if low < high:
        piv = partition(arr, low, high)
        quicksort(arr,low,piv-1)
        quicksort(arr, piv+1, high)

def ratakan (listnya):
    if isinstance(listnya, list):
        temp = []
        for i in listnya:
            temp.extend(ratakan(i))
        return temp
    else:
        return [listnya]
 
listnya = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
 
arr= ratakan (listnya)
quicksort(arr, 0, len(arr)-1)

print("Sebelum quicksort = ",listnya) 
print("Setelah quicksort = ", arr) 
    
