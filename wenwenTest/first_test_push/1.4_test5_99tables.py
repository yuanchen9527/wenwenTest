# encoding: utf-8
for a in range(1, 10):
    for b in range(1,10):
        product = a*b
        print(str(a) + "*" + str(b) + "=" + str(product),end=" ")
        if b == 9:
            print("\n")

