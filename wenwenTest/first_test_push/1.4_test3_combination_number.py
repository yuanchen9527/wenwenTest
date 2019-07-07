# encoding: utf-8
hundreds = [1, 2, 3, 4]
tens = [1, 2, 3, 4]
units = [1, 2, 3, 4]
for a in hundreds:
    for b in tens:
        for c in units:
            number = 100*a+10*b+c
            print(number)

