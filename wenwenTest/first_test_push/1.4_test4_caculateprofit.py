# encoding: utf-8
commission = float(input("Please input commission:"))
reward0_10 = 0.1*10
reward10_20 = reward0_10 + 0.075*20
reward20_40 = reward10_20 + 20*0.05
reward40_60 = reward20_40 + 0.03*20
reward60_100 = reward40_60 + 0.015*40
if commission <= 10:
    reward = 0.1*commission
    print("奖金为：" + str(reward))
elif 10 < commission <= 20:
    reward = reward0_10 + 0.075*(commission-10)
    print("奖金为：" + str(reward))
elif 20 < commission <=40:
    reward = reward10_20 + 0.05*(commission-20)
    print("奖金为：" + str(reward))
elif 40 < commission <=60:
    reward = reward20_40 + 0.03*(commission-40)
    print("奖金为：" + str(reward))
elif 60 < commission <=100:
    reward = reward40_60 + 0.015*(commission-60)
    print("奖金为：" + str(reward))
elif commission > 100:
    reward = reward60_100 + 0.01*(commission-100)
    print("奖金为：" + str(reward))

