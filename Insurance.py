import InsureInFlowPV as IIP
import InsureOutFlowPV as IOP
import matplotlib.pyplot as plt
import numpy as np
def main():
    rate1 = []
    rate2 = []
    x = list(range(26,105))
    for i in range(26,105):
        rate1.append(IIP.InsureInFlowPV(Rate=0.03,DeadAge=i) - IOP.InsureOutFlowPV(Rate=0.03,DeadAge=i))
        rate2.append(IIP.InsureInFlowPV(Rate=0.04,DeadAge=i) - IOP.InsureOutFlowPV(Rate=0.04,DeadAge=i))
    print('贴现率r=0.3:\n',rate1)
    print('贴现率r=0.4:\n',rate2)
    plt.plot(x,rate1,label='r=0.03')
    plt.plot(x,rate2,label='r=0.04')
    plt.plot(x,np.zeros_like(x),':')
    plt.title('InsureFlow')
    plt.xlabel('DeadAge')
    plt.ylabel('PV')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()