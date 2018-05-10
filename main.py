def partition(a, l, r):
    x = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def kthlargest(a, k):
    l = 0
    r = len(a) - 1
    split_point = partition(a, l, r)
    if split_point == r - k + 1:
        result = a[split_point]
    elif split_point > r - k + 1:
        result = kthlargest(a[:split_point], k - (r - split_point + 1))
    else:
        result = kthlargest(a[split_point + 1:r + 1], k)
    return result


a = [1, 3, 2, 5, 7, 6, 8, 9, 4]
print(kthlargest(a, 4))
