a=0.5
#First Weights
b1=0.3
w11=0.05
w12=0.2

#Second Weights
b2=0.15
w21=0.1
w22=0.2

#Third Weights
b3=0.5
v1=0.5
v2=0.5

gate = input("Enter the name of the Gate: ")
print("Enter the TRUTH TABLE for", gate, ":=")

#Taking Inputs
print("Enter x1: ")
x1 = list(map(int, input().split(' ')))

print("Enter x2: ")
x2 = list(map(int, input().split(' ')))

print("Enter Output: ")
t = list(map(int, input().split(' ')))

i = 0
while i <= 3:
    #First we will calculate Zin
    zin1 = b1 + (w11 * x1[i]) + (w12 * x2[i])
    zin2 = b2 + (w21 * x1[i]) + (w22 * x2[i])
    if(zin1 >= 0):
        z1 = 1
    else:
        z1 = -1

    if (zin2 >= 0):
        z2 = 1
    else:
        z2 = -1
    #Now we will calculate Yin
    yin = b3 + (v1 * z1) + (v2 * z2)
    if (yin >= 0):
        y = 1
    else:
        y = -1

    #Now we will update the Weights

    if(t[i] == y):
        #No Weights will be update
        print("No weights Change Occurs")

    elif(t[i] == 1):
        #Update weights on ZJ, the unit whose net input is closest to 0
        zin = min(zin1, zin2, key = abs)
        if(zin1 == zin):
            b1 = b1 + a * (1 - zin1)
            w11 = w11 + a * (1 - zin1) * x1[i]
            w12 = w12 + a * (1 - zin1) * x2[i]

        else:

            b2 = b2 + a * (1 - zin2)
            w21 = w21 + a * (1 - zin2) * x1[i]
            w22 = w22 + a * (1 - zin2) * x2[i]


    else:
        #update weights on all units that have positive net input

        if (zin1 > 0):
            b1 = b1 + a * (-1 - zin1)
            w11 = w11 + a * (-1 - zin1) * x1[i]
            w12 = w12 + a * (-1 - zin1) * x2[i]

        if(zin2 > 0):
            b2 = b2 + a * (-1 - zin2)
            w21 = w21 + a * (-1 - zin2) * x1[i]
            w22 = w22 + a * (-1 - zin2) * x2[i]

    print("New Weights will be: (", w11, w12, b1, "), (", w21, w22, b2, "), (", v1, v2, b3, ")")

    i+=1
