def pairInSortedRotated(arr, target):
    n = len(arr)

    # Find the pivot (smallest element)
    pivot = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i + 1
            break

    low = pivot
    high = (pivot - 1 + n) % n

    while low != high:
        current_sum = arr[low] + arr[high]

        if current_sum == target:
            return True

        elif current_sum < target:
            low = (low + 1) % n

        else:
            high = (high - 1 + n) % n

    return False


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(pairInSortedRotated(arr, target))