import matplotlib.pyplot as plt
from math import factorial
kol_kanalov=15
graph_och = []
graph_n = []
graph_kz = []
graph_Mn = []
graph_Mq = []
lambbda = 2.5
mu = 1.09
nu = 0.54
for n in range(1,kol_kanalov+1):
    graph_n.append(n)
    print(f'Кол-во каналов - {n}:')
    znam = 0
    kPn = 0
    for i in range(n+1): 
        kPi = (lambbda**i)/(factorial(i)*(mu**i))
        znam += kPi
        if i == n: kPn = kPi
        #print(znam)
    znam1 = 0
    chast_Mq = 0
    kPm_cur = lambbda**1/(n*mu+1*nu)**1 * kPn
    znam1 += kPm_cur
    chast_Mq += kPm_cur
    #print(znam1)
    for i in range(2,15):
        mnoj = lambbda/(n*mu+i*nu)
        #print(f'{i} mnoj = ',mnoj)
        Pm_cur = mnoj * kPm_cur
        kPm_cur = Pm_cur
        znam1+=Pm_cur
        chast_Mq+=Pm_cur * i
    znam+=znam1
    P = 1/znam
    Mn = 0
    Mq = 1
    Mn+=n*P*znam1
    Mq*=chast_Mq*P
    #print(f'P0 = {P}')
    sum = 0
    P_och = 0
    for i in range(n+1):
        Pi = ((lambbda**i)/(factorial(i)*(mu**i)))*P
        #print(f"P{i} = {Pi}")
        Mn+=Pi*i
        #sum+=Pi
        if i == n:
            print(Pi)
            P_och = P*znam1
    kz = Mn/n
    '''
    print(f'sum_p = {sum}') 
    print(f'Мат. ожидание = {round(Mn,3)}')
    print(f'{round(Mn,3)}')
    print(f'Коэфф. нагруж. = {round(kz,3)}')
    print(f'{round(kz,3)}')
    print(f'Вер. сущ. очереди = {round(P_och,3)}')
    print(f'{round(P_och,3)}')
    print(f'Мат. ожидание длины очереди = {round(Mq,3)}')
    print(f'{round(Mq,3)}')
    '''
    graph_Mn.append(Mn)
    graph_kz.append(kz)
    graph_och.append(P_och)
    graph_Mq.append(Mq)

plt.plot(graph_n, graph_Mn)
plt.xlabel("n")
plt.ylabel("M(n)")
plt.grid()
plt.show()
plt.plot(graph_n, graph_kz)
plt.xlabel("n")
plt.ylabel("kз")
plt.grid()
plt.show()
plt.plot(graph_n, graph_och)
plt.xlabel("n")
plt.ylabel("Pоч")
plt.grid()
plt.show()
plt.plot(graph_n, graph_Mq)
plt.xlabel("n")
plt.ylabel("Mq")
plt.grid()
plt.show()


