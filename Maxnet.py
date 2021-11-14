#Error
e = float(input("Enter Error Value: "))
b = [0,0,0,0]

#wights Initilize
print("Enter Weights: ")
a = list(map(float, input().split(' ')))
length = len(a)
i = 0
while(i < length):
    k = 0
    sum = 0.0
    while(k < length):
        if (k != i):
            sum += a[k]
        k += 1
    b[i] = (a[i] - (e * sum))
    if(b[i] < 0):
        b[i] = 0
    else:
        b[i] = b[i]
    i += 1

a = b[:]
print("New Weights: ")
j = 0
while(j <= 3):
    print(round(a[j], 2))
    j += 1