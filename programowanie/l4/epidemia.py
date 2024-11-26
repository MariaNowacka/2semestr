#N to wielkość populacji,
#β to wskaźnik infekcjii (tempo jej rozprzestrzeniania się),
#σ to wskaźnik ikubacji (średni czas inkubacji to 1/σ),
#γ to wskaźnik wyzdrowień (jeśli średni czas infekcji wynosi D, wówczas γ = 1/D).
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import sys
# 1000, 999, 1, 0, 0, 1.34, 0.19, 0.34
N=float(sys.argv[1])

beta = float(sys.argv[6])
sigma = float(sys.argv[7])
gamma = float(sys.argv[8])
S0=float(sys.argv[2])
E0=float(sys.argv[3])
I0=float(sys.argv[4])
R0=float(sys.argv[5])
t = np.linspace(0,100)
def d(zmienne, t):
      S, E, I, R = zmienne
      dSdt = -beta*S*I/N
      dEdt = beta*S*I/N - sigma*E
      dIdt = sigma*E - gamma*I
      dRdt = gamma*I
      return [dSdt, dEdt, dIdt, dRdt]
  
i = S0, E0, I0, R0
r= odeint(d, i, t)

S=r[:,0]
E=r[:,1]
I=r[:,2]
R=r[:,3]

def susceptible(S,I):
    dSdt = -beta*S*I/N
    return dSdt

def exposed(S, I, E):
  dEdt = beta*S*I/N - sigma*E
  return dEdt

def infected(E,I):
  dIdt = sigma*E - gamma*I
  return dIdt

def recovered(I):
  dRdt = gamma*I
  return dRdt
'''S = odeint(susceptible,S0,t)
E = odeint(exposed,S0,E0,t)
I = odeint(infected,I0, t)
R = odeint(recovered,R0,t)'''


plt.plot(t,S,label="S - zdrowi")
plt.plot(t,E, label="E - zarażeni, niezarażający")
plt.plot(t,I, label="I - zarażeni, zarażający")
plt.plot(t,R, label="R - ozdrowieni")

plt.xlabel('czas')
plt.ylabel('Liczba ludności')
plt.legend()
plt.savefig(r"C:\Users\dell\AppData\Local\Programs\Python\Python310\f4.png")
plt.show()
