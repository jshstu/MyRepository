# -*- coding: utf-8 -*-
import numpy as np
import numpy.matlib as matlib
def InsureInFlowPV(StartPayAge=25 , DeadAge=100, OutPayment =8000, Rate =0.03):
    # 支付金额的增长率
    temppay = np.arange(1, 1.08, 0.01)
    # 矩阵化处理,每三年支付金额增长0.01%
    temppay = matlib.repmat(temppay, 5, 1)  # remat复制数组  reshape重组数组
    tempay = np.reshape(temppay, (1, 45), 'F')
    # 收入初始矩阵
    InPayment = np.array([0] * 100)
    InPayment[-41:] = 2e4 * tempay[:, :-4]
    # %%
    if DeadAge <= StartPayAge:
        print("DeadAge must bigger than StartPayAge")
    elif StartPayAge < DeadAge & DeadAge <= 50:
        PV = max(((DeadAge - StartPayAge) * OutPayment + 2e5) / (1 + Rate) ** (DeadAge - StartPayAge),
                 np.pv(Rate, DeadAge - StartPayAge, OutPayment))
    elif 50 < DeadAge & DeadAge < 60:
        PV = max((4e5) / (1 + Rate) ** (DeadAge - StartPayAge), np.pv(Rate, 25, OutPayment))
    elif 60 <= DeadAge & DeadAge < 80:
        PV = np.npv(Rate, InPayment[59:DeadAge]) / (1 + Rate) ** 35 + max(0, (334200 - sum(InPayment[59:DeadAge]))) / (
                    1 + Rate) ** (DeadAge - 35)
    elif 80 <= DeadAge & DeadAge < 88:
        PV = np.npv(Rate, InPayment[59:DeadAge]) / (1 + Rate) ** 35
    else:
        PV = np.npv(Rate, InPayment[59:DeadAge]) / (1 + Rate) ** 35 + 1e5 / (1 + Rate) ** 63
    return PV

#print(InsureInFlowPV())
