import matplotlib.pyplot as plt
def factorial(n):
    if n ==0: 
        return 1
    else:
        return n*factorial(n-1)
kol_kanalov=15
graph_och = []
graph_n = []
graph_kz = []
graph_Mn = []
graph_Mq = []
lambbda = 2.5
mu = 1.09
for n in range(3,kol_kanalov+1):
    a = lambbda/(n*mu)
    print(a)
    graph_n.append(n)
    print(f'Кол-во каналов - {n}:')
    znam = 0
    for i in range(n+1): 
        znam += (lambbda**i)/(factorial(i)*(mu**i))
        #print(znam)
    znam+=(lambbda**(n))/(factorial(n)*(mu**n))*a/(1-a)
    #print(znam)
    P = 1/znam
    print(f'P0 = {P}')
    sum = 0
    Mn = 0
    Mq = 0
    P_och = 0
    for i in range(n+1):
        Pi = ((lambbda**i)/(factorial(i)*(mu**i)))*P
        print(f"P{i} = {Pi}")
        Mn+=Pi*i
        sum+=Pi
        if i == n:
            P_och = Pi*n/(n-(lambbda/mu))
            Mn+=n*Pi*a/(1-a)
            Mq = Pi*a/(1-a)**2        
    #print(f'sum_p = {sum}') 
    #print(f'Мат. ожидание = {round(Mn,3)}')
    print(f'{round(Mn,3)}')
    graph_Mn.append(Mn)
    kz = Mn/n
    #print(f'Коэфф. нагруж. = {round(kz,3)}')
    print(f'{round(kz,3)}')
    graph_kz.append(kz)
    #print(f'Вер. сущ. очереди = {round(P_och,3)}')
    print(f'{round(P_och,3)}')
    graph_och.append(P_och)
    #print(f'Мат. ожидание длины очереди = {round(Mq,3)}')
    print(f'{round(Mq,3)}')
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
