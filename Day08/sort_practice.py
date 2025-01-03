# 快速排序
def partition(arr, left, right):
    k = i = left
    while i < right:
        if arr[i] < arr[right]:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
        i += 1
    arr[k], arr[right] = arr[right], arr[k]
    return k


def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)


def adjust_heap(arr, pos, length):
    son = pos*2+1
    while son < length:
        if length > son + 1 and arr[son+1] > arr[son]:
            son += 1
        if arr[son] > arr[pos]:
            arr[son], arr[pos] = arr[pos], arr[son]
            pos = son
            son = pos * 2 + 1
        else:
            break


def heap_sort(arr):
    for i in range(len(arr)//2-1,-1,-1):
        adjust_heap(arr, i, len(arr))
    arr[0],arr[len(arr)-1] = arr[len(arr)-1],arr[0]
    for arr_len in range(len(arr)-1,1,-1):
        adjust_heap(arr, 0, arr_len)
        arr[0], arr[arr_len - 1] = arr[arr_len - 1], arr[0]

if __name__ == '__main__':
    # 快速排序
    arr = [3, 87, 2, 93, 78, 56, 61, 38, 12, 40]
    # quick_sort(arr, 0, 9)
    print(arr)
    heap_sort(arr)
    print(arr)