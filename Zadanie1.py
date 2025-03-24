import matplotlib.pyplot as plt
def factorial(n):
    if n ==0: 
        return 1
    else:
        return n*factorial(n-1)
kol_kanalov=7
graph_otk = []
graph_n = []
graph_kz = []
graph_Mn = []
lambbda = 2.5
mu = 1.09
for n in range(5,kol_kanalov+1):
    graph_n.append(n)
    print(f'Кол-во каналов - {n}:')
    znam = 0
    for i in range(n+1):
        znam += (lambbda**i)/(factorial(i)*(mu**i))
        #print(znam)
    P = 1/znam
    #print(f'P0 = {P}')
    sum = 0
    Mn = 0
    for i in range(n+1):
        Pi = ((lambbda**i)/(factorial(i)*(mu**i)))*P
        print(f"P{i} = {Pi}")
        Mn+=Pi*i
        sum+=Pi
        if i == n:
            print(f'Вер. отк. = {Pi}')
            graph_otk.append(Pi)        
    print(f'sum_p = {sum}') 
    print(f'Мат. ожидание = {Mn}')
    graph_Mn.append(Mn)
    kz = Mn/n
    graph_kz.append(kz)
    print(f'Коэфф. нагруж. = {kz}')
'''plt.plot(graph_n, graph_otk)
plt.xlabel("n")
plt.ylabel("Pотк")
plt.grid()
plt.show()
plt.plot(graph_n, graph_Mn)
plt.xlabel("n")
plt.ylabel("M(n)")
plt.grid()
plt.show()
plt.plot(graph_n, graph_kz)
plt.xlabel("n")
plt.ylabel("kз")
plt.grid()
plt.show()'''