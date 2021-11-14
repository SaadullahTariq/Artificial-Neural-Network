#Sigma Rule Implementation
def sigma(k, last, x, i):
    sum = 0
    while(k <= last):
        index = int(i + k)
        if(0 < index <= 7):
            index -= 1
            sum += x[index]
        k += 1
    return sum
#Signal
print("Enter Signal: ")
signal = list(map(float, input().split(' ')))
length = len(signal)
x = [0] * length
if(length % 2 == 0):
    print("No Solution exist for THIS! Because List is not Identical")
else:
    center = int((length / 2))
    a = 0
    last = int(length - 1)
    check = 0
    while(a < center):
        second = int(last - a)
        if(signal[a] == signal[second]):
            check = 1
        else:
            check = 0
        a += 1
    if(check == 1):
        # C1 and C2
        c1 = float(input("Enter C1: "))
        c2 = float(input("Enter C2: "))
        # R1 and R2
        r1 = int(input("Enter R1: "))
        r2 = int(input("Enter R2: "))
        if (r1 < r2 and c1 > 0 and c2 < 0):
            tmax = int(input("Enter Tmax: "))
            t = 1
            while (t < tmax):
                print("======")
                print("t =", t)
                print("======")
                m = 0
                i = 1
                while (m < length & i <= length):
                    # Formula Starts from Here
                    sum1 = sigma(-r1, r1, signal, i)
                    sum2 = sigma(-r2, (-r1 - 1), signal, i)
                    sum3 = sigma((r1 + 1), r2, signal, i)
                    x[m] = (c1 * sum1) + (c2 * sum2) + (c2 * sum3)
                    m += 1
                    i += 1
                l = 0
                while (l < length):
                    print(round(x[l], 2))
                    l += 1
                signal = x[:]
                t += 1
        else:
            print("No solution exist for this! because R1 have greater value")
    else:
        print("There is no Solution because List is not Identical!")