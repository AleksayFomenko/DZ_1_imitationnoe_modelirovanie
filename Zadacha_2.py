import matplotlib.pyplot as plt
from math import factorial

def obr_fact(n, k):
    if n == 0 or k == 0:
        return 1
    for i in range(1, k + 1):
        if i == 1:
            result = n  # Для i = 1
        else:
            result = n
            for j in range(1, i):
                result *= (n - j)  # n * (n-1) * (n-2) * ... * (n-(i-1))
    return result
n = 42 
lambbda = 0.526
mu = 1.5
m_kol = 40
m_mas = []
M_prostoim = []
M_ojidm = []
P_ojidm = []
M_zan_nm = []
kzm = []
for m in range(1,m_kol+1):
    m_mas.append(m)
    k = 0
    stepen = 0
    M_prostoi = 0
    M_ojid = 0
    P_ojid = 0
    M_zan_n = 0
    kz = 0
    koef = [1]
    for  i in range(1,n+1):
        if k < m:
            k+=1
            Pi = obr_fact(n,i)/factorial(k) * (lambbda/mu)**(i)
            koef.append(Pi) 
        else:
            stepen += 1
            denominator = ((factorial(m))*(m**(stepen)))
            Pi = obr_fact(n,i)/denominator * (lambbda/mu)**(i)
            koef.append(Pi) 
    #print(koef)
    P0 = 1/sum(koef)
    print(P0)
    for i in range(0,len(koef)):
        koef[i]*=P0
    #print(sum(koef))
    for i in range(n,-1,-1):
        M_prostoi += i * koef[n-i] # станки в простое
        #print(koef[n-i], i)
    for i in range(1,n-m+1):
        #print(i, i+m)
        M_ojid+=koef[i+m]*i
        P_ojid+=koef[i+m]
    k = 0
    for i in range(n+1):
        if k!= m:
            M_zan_n += koef[i] * k
            k+=1
        else:
            M_zan_n += koef[i] * k
    kz = M_zan_n/m
    M_prostoim.append(M_prostoi)
    M_ojidm.append(M_ojid)
    P_ojidm.append(P_ojid)
    M_zan_nm.append(M_zan_n)
    kzm.append(kz)

plt.plot(m_mas, M_prostoim)
plt.xlabel("m")
plt.ylabel("M(N)")
plt.grid()
plt.show()
plt.plot(m_mas, M_ojidm)
plt.xlabel("m")
plt.ylabel("M(Q)")
plt.grid()
plt.show()
plt.plot(m_mas, P_ojidm)
plt.xlabel("m")
plt.ylabel("Pо")
plt.grid()
plt.show()
plt.plot(m_mas, M_zan_nm)
plt.xlabel("m")
plt.ylabel("M(m)")
plt.grid()
plt.show()
plt.plot(m_mas, kzm)
plt.xlabel("m")
plt.ylabel("kз")
plt.grid()
plt.show()