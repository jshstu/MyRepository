import numpy as np
def InsureOutFlowPV(StartPayAge=25, EndPayAge=50, DeadAge=100, OutPayment=8000, Rate=0.03):
    # 如果死亡年龄小于保费支出起始年龄,本案例为25
    if DeadAge < StartPayAge:
        #输出问题
        print ("deadage must bigger than startpayage")
    elif DeadAge < EndPayAge:
        PV = abs(np.pv(Rate, DeadAge - StartPayAge, OutPayment))
    else:
        PV = abs(np.pv(Rate, EndPayAge - StartPayAge, OutPayment))
    return PV
