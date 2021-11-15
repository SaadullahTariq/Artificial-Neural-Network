a=1
theeta = 0.2
b=w1=w2=yin=net=0
y_arr = [0] * 4
yin_arr = [0] * 4
w1_arr = [0] * 4
w2_arr = [0] * 4
b_arr = [0] * 4
w1ch_arr = [0] * 4
w2ch_arr = [0] * 4
bch_arr = [0] * 4
gate = input("Enter the name of the Gate: ")
print("Enter the TRUTH TABLE for", gate, ":=")
print("Enter x1: ")
x1 = list(map(int, input().split(' ')))
print("Enter x2: ")
x2 = list(map(int, input().split(' ')))
print("Enter Output: ")
t = list(map(int, input().split(' ')))
i = 0
while i <= 3:
    if (t[i] == 0):
        t[i] = -1
    i += 1
i = 0
while i <= 3:
    w1c = a * x1[i] * t[i]
    w1ch_arr[i] = w1c
    w2c = a * x2[i] * t[i]
    w2ch_arr[i] = w2c
    bch = a * t[i]
    bch_arr[i] = bch
    yin = b + (w1 * x1[i]) + (w2 * x2[i])
    yin_arr[i] = yin
    print("Yin: ", yin)
    if (yin > theeta):
        y = 1
    elif (theeta > yin > -theeta):
        y = 0
    else:
        y = -1
    y_arr[i] = y
    print("Y: ", y)
    print("t: ", t[i])
    if (y != t[i]):
        w1 = w1 + x1[i] * a * t[i]
        w2 = w2 + x2[i] * a * t[i]
        b = b + a * t[i]
        print("w1 = w1 + x1 * a * t = ", w1)
        print("w2 = w2 + x2 * a * t = ", w2)
        print("b = b + a * t = ", b)
        print("New Matrix of weights is: (", w1, w2, b, ")")
        print("------------------------------------")
    else:
        w1 = w1
        w2 = w2
        b = b
        print("w1 = w1 = ", w1)
        print("w2 = w2 = ", w2)
        print("b = b  = ", b)
        print("New Matrix of weights is: (", w1, w2, b, ")")
        print("------------------------------------")

    w1_arr[i] = w1
    w2_arr[i] = w2
    b_arr[i] = b
    i += 1


print("x1\t|\tx2\t|\t1\t|\tYin\t|\tY\t|\tΔw1\t\tΔw2\t\tΔb\t|\tw1\t\tw2\t\tb")
j = 0
while j <= 3:
    print(x1[j], "\t|\t", x2[j], "\t|\t", 1, "\t|\t", yin_arr[j], "\t|\t", y_arr[j], "\t|\t", w1ch_arr[j], "\t\t",w2ch_arr[j],
          "\t\t", bch_arr[j], "\t|\t", w1_arr[j], "\t\t", w2_arr[j], "\t\t", b_arr[j])
    j += 1
