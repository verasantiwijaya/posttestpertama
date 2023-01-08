def mergesort(arr):#bagi list
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 #variable mecah list
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge (left,right)

def merge(left, right):
    result = []#list kosong untuk nampung nilai

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    elif right:
        result += right
    return result

def ratakan (listnya):
    if isinstance(listnya, list):
        temp = []
        for i in listnya:
            temp.extend(ratakan(i))
        return temp
    else:
        return [listnya]
 
listnya = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
 
res = ratakan (listnya)
hasil = mergesort(res)

print("Sebelum mergesort = ",listnya) 
print("Setelah mergesort = ", hasil) 