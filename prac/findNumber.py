#!/bin/python3
def findNumber(arr, k):
    if k in arr:
        return True
    return False

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)
    k = int(input().strip())
    print(findNumber(arr, k))
