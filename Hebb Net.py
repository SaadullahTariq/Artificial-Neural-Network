
#Initialize all weights
b=w1=w2=0

#Enter the Input
print("Enter x1: ")
x1 = list(map(int, input().split(' ')))
print("Enter x2: ")
x2 = list(map(int, input().split(' ')))
print("Enter Target: ")
y = list(map(int, input().split(' ')))
len = len(x1)
i = 0
while i < len:
    if (y[i] == 0):
        y[i] = -1
    i += 1
print("=========================================")
print("X1\tX2\t1\t T\tΔW1\tΔW2\tΔb\tW1\tW2\tb")
i = 0
while i < len:
    delta_w1 = x1[i] * y[i]
    delta_w2 = x2[i] * y[i]
    delta_b = y[i]
    w1 += delta_w1
    w2 += delta_w2
    b += delta_b
    print(x1[i],"\t", x2[i], "\t1\t", y[i], "\t", delta_w1, "\t", delta_w2, "\t", delta_b, "\t", w1, "\t", w2, "\t", b)
    i += 1