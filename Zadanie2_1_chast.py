import matplotlib.pyplot as plt
def factorial(n):
    if n ==0: 
        return 1
    else:
        return n*factorial(n-1)

kol_kanalov = 15
kol_ochered = 15
name_x = 'm'
name_var = 'n'
graph_n = []
graph_m = []
graph_otk = []
graph_Mn = []
graph_kz = []
graph_och = []
graph_Mq = []
graph_kzMq = []
lambbda = 2.5
mu = 1.09
for n in range(1, kol_kanalov+1):
    graph_n.append(n)
    graph_m = []
    graph_m_otk = []
    graph_m_Mn = []
    graph_m_kz = []
    graph_m_och = []
    graph_m_Mq = []
    graph_m_kzMq = []
    for m in range(1,kol_ochered+1):
        graph_m.append(m)
        a = lambbda/(n*mu)
        print(a)
        print(f'Кол-во каналов - {n}:')
        znam = 0
        for i in range(n+1): 
            znam += (lambbda**i)/(factorial(i)*(mu**i))
            #print(znam)
        for i in range(1,m+1):
            znam+=(lambbda**(n))/(factorial(n)*(mu**n))*a**i
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
            if i == n:                                # Работа с Pn 
                P_otk = (a**m) * Pi
                #P_och = Pi*(1-a**m)/(1-a)
                for j in range(1,m+1):
                    P_och += Pi*a**j
                    Mn += n*Pi*a**j
                    Mq += Pi*j*a**j        
        print(f'Для n = {n}, m = {m}:')
        print(f'Вер. отказа = {round(P_otk,3)}')
        graph_m_otk.append(P_otk)
        #print(f'sum_p = {sum}') 
        print(f'Мат. ожидание = {round(Mn,3)}')
        #print(f'{round(Mn,3)}')
        graph_m_Mn.append(Mn)
        kz = Mn/n
        print(f'Коэфф. нагруж. = {round(kz,3)}')
        #print(f'{round(kz,3)}')
        graph_m_kz.append(kz)
        print(f'Вер. сущ. очереди = {round(P_och,3)}')
        #print(f'{round(P_och,3)}')
        graph_m_och.append(P_och)
        #print(f'Мат. ожидание длины очереди = {round(Mq,3)}')
        #print(f'{round(Mq,3)}')
        graph_m_Mq.append(Mq)
        kz_Mq = Mq/m
        print(f'Коэфф. очереди = {round(kz_Mq,3)}')
        #print(f'{round(kz_Mq,3)}')
        graph_m_kzMq.append(kz_Mq)
    graph_otk.append(graph_m_otk)
    graph_Mn.append(graph_m_Mn)
    graph_kz.append(graph_m_kz)
    graph_och.append(graph_m_och)
    graph_Mq.append(graph_m_Mq)
    graph_kzMq.append(graph_m_kzMq)
print(graph_kz[0])
for i in range(len(graph_otk)):
    plt.plot(graph_m, graph_otk[i], label = f'{name_var} = {i+1}')
plt.xlabel(f"{name_x}")
plt.ylabel("Pотк")
plt.grid()
plt.legend()
plt.show()

for i in range(len(graph_Mn)):
    plt.plot(graph_m, graph_Mn[i], label = f'{name_var} = {i+1}')
plt.xlabel(f"{name_x}")
plt.ylabel("Mn")
plt.grid()
plt.legend()
plt.show()

for i in range(len(graph_kz)):
    plt.plot(graph_m, graph_kz[i], label = f'{name_var} = {i+1}')
plt.xlabel(f"{name_x}")
plt.ylabel("kз")
plt.grid()
plt.legend()
plt.show()

for i in range(len(graph_och)):
    plt.plot(graph_m, graph_och[i], label = f'{name_var} = {i+1}')
plt.xlabel(f"{name_x}")
plt.ylabel("Pоч")
plt.grid()
plt.legend()
plt.show()

for i in range(len(graph_Mq)):
    plt.plot(graph_m, graph_Mq[i], label = f'{name_var} = {i+1}')
plt.xlabel(f"{name_x}")
plt.ylabel("Mq")
plt.grid()
plt.legend()
plt.show()

for i in range(len(graph_kzMq)):
    plt.plot(graph_m, graph_kzMq[i], label = f'{name_var} = {i+1}')
plt.xlabel(f"{name_x}")
plt.ylabel("kзq")
plt.grid()
plt.legend()
plt.show()


