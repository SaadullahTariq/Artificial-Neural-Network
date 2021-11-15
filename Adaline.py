a=0.2
b=-1.5
w1=1
w2=1
yin=net=delta=0
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
length = len(t)
i = 0
while i < length:
    if (t[i] == 0):
        t[i] = -1
    i += 1

i = 0
while i < length:
    yin = b + (w1 * x1[i]) + (w2 * x2[i])
    yin_arr[i] = yin
    w1c = a * x1[i] * (t[i] - yin)
    w1ch_arr[i] = w1c
    w2c = a * x2[i] * (t[i] - yin)
    w2ch_arr[i] = w2c
    bch = a * (t[i] - yin)
    bch_arr[i] = bch
    print("Yin: ", yin)
    if (yin > 0):
        y = 1
    else:
        y = -1
    y_arr[i] = y
    print("Y: ", y)
    print("t: ", t[i])
    if ((t[i] - yin) != 0):
        w1 = w1 + x1[i] * (t[i] - yin) * a
        w2 = w2 + x2[i] * (t[i] - yin) * a
        b = b + a * (t[i] - yin)
        print("w1 + w1 + x1 * (t - yin) * a = ", w1)
        print("w2 = w2 + x2 * (t - yin) * a = ", w2)
        print("b =  b + a * (t - yin) = ", b)
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
