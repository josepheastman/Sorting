# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr


def merge_sort2(arr):
    # merge_sort no helper function
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort2(left)
        merge_sort2(right)

        i = j = y = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[y] = left[i]
                i += 1
            else:
                arr[y] = right[j]
                j += 1
            y += 1

        while i < len(left):
            arr[y] = left[i]
            i += 1
            y += 1

        while j < len(right):
            arr[y] = right[j]
            j += 1
            y += 1

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
