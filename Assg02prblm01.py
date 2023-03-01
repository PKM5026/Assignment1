X = [(2,5), (1,2), (4,4), (2,3), (2, 1)]
Y = len(X)
for i in range(0, Y):
    for j in range(0, Y - i - 1):
        if (X[j][-1]> X[j +1][-1]):
            Values = X[j]
            X[j] = X[j+1]
            X[j+1] = Values
print(X)