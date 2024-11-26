#N to wielkość populacji,
#β to wskaźnik infekcjii (tempo jej rozprzestrzeniania się),
#σ to wskaźnik ikubacji (średni czas inkubacji to 1/σ),
#γ to wskaźnik wyzdrowień (jeśli średni czas infekcji wynosi D, wówczas γ = 1/D).
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import sys, argparse
# 1000, 999, 1, 0, 0, 1.34, 0.19, 0.34

parser = argparse.ArgumentParser()
#parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
parser.add_argument('-N',dest="N", type=int, default=1000)
parser.add_argument('-S0',dest="S0", type= int, default=999)
parser.add_argument('-E0',dest="E0", type= int, default=1)
parser.add_argument('-I0',dest="I0", type= int, default=0)
parser.add_argument('-R0',dest="R0", type= int, default=0)
parser.add_argument('-beta',dest="beta", type= float, default=1.34)
parser.add_argument('-sigma',dest="sigma", type= float, default=0.19)
parser.add_argument('-gamma',dest="gamma", type= float, default=0.34)
args = parser.parse_args()

N=args.N
beta = args.beta
sigma = args.sigma
gamma = args.gamma
S0=args.S0
E0=args.E0
I0=args.I0
R0=args.R0

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

plt.plot(t,S,label="S - zdrowi")
plt.plot(t,E, label="E - zarażeni, niezarażający")
plt.plot(t,I, label="I - zarżeni, zarażający")
plt.plot(t,R, label="R - ozdrowieni")

plt.xlabel('czas')
plt.ylabel('Liczba ludności')
plt.legend()
plt.savefig(r"C:\Users\dell\AppData\Local\Programs\Python\Python310\2.png")
plt.show()

