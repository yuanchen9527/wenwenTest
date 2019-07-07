# encoding: utf-8
# @Time   : 2019/6/17 7:03
# def true():
#     print("true")
#     return True
# def false():
#     print("false")
#     return False
# true() and false()
#for in循环测试
# for i in range(0,10):
#     if i % 2 !=0:
#         print(i)
#         break
#         print("break")
for i in range(0,100):
    print(i)
    if i % 2 != 0:
        continue
        print('continue')
    print(i+1)