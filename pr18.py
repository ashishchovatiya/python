# a=[[1,2,3],[4,5,6]]
# b=[[7,8,9,10],[11,12,13,14],[15,16,17,18]]

def matrix(row, column):
    p = []
    print('Enter elements row wise')
    for i in range(row):
        q = []
        for j in range(column):
            k = int(input())
            q.append(k)
        p.append(q.copy())
        q.clear()
    return p

print("1st matrix:")
i, j = map(int, input("enter row and column=").split(" "))
a = matrix(i, j)
print("2st matrix:")
i, j = map(int, input("enter row and column=").split(" "))
b = matrix(i, j)

def product(m, n):
    r = []
    if len(m[0]) == len(n):
        for i in range(len(m)):
            t = []
            for j in range(len(n[i])):
                sum = 0
                for k in range(len(m[i])):
                    sum += m[i][k] * n[k][j]
                t.append(sum)
            r.append(t.copy())
            t.clear()
        return r
    else:
        print("Can't Multiply !!!!")
        print('Column of 1st Matrix and Row od 2nd Martix should be same')
        pass
c = product(a, b)
print(c)