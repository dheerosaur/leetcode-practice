def remove_element(A, n):
    k = 0
    for i, num in enumerate(A):
        if num != n:
            A[k] = A[i]
            k += 1
    return A


def move_to_end1(A, n):
    k = 0
    for i, num in enumerate(A):
        if num != n:
            A[k], A[i] = A[i], A[k]
            k += 1
    return A


def move_to_end2(A, n):
    low, high = 0, len(A) - 1
    while low < high:
        if A[high] == n:
            high -= 1
        elif A[low] == n:
            A[high], A[low] = A[low], A[high]
            low, high = low + 1, high - 1
        else:
            low += 1
    return A


A = [2, 1, 1, 3, 1, 4, 1, 1]
print(remove_element(A, 1))

A = [2, 1, 1, 3, 1, 4, 1, 1]
print(move_to_end1(A, 1))

A = [2, 1, 1, 3, 1, 4, 1, 1]
print(move_to_end2(A, 1))
