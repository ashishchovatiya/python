def arr(q, s):
    l = len(q) // 2
    if s < q[l]:
        p = arr(q[:l], s)
    elif s > q[l]:
        p = arr(q[l:], s) + l
    elif s == q[l]:
        return l + 1
    return p


l1 = [1, 23, 34, 45, 56, 67, 78, 89, 98, 100]
print(l1)
s = int(input("enter the search number="))
print(arr(l1, s))
