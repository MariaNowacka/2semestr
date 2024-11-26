import networkx as nx
import matplotlib.pyplot as plt
import random
import imageio.v2 as imageio 
def graf(rodzaj, n, p=0.3,k=2):
  ''' rodzaj : R, W, B 
      n - ilosc wierzchołków
      p - prawdopodobienstwo
      k0 - ile krawędzi rysuje'''
  if rodzaj == "R":
    # n=6 i p=0.4
    G=nx.erdos_renyi_graph(n, p, seed=None, directed=False)
    #nx.draw(R)
    #nazwa="R"
  elif rodzaj == "W":
    #n=6, k=2 i p=0.3
    G=nx.watts_strogatz_graph(n,k,p)
    #nazwa="W"
  elif rodzaj == "B":
    G=nx.extended_barabasi_albert_graph(n, k, p, 0.3, seed=None)
  else : 
    print("nieopowiednie parametry czy coś")
  kroki=10
  agent=0
  poz=nx.spring_layout(G)
  wierzcholki=[]
  for i in range(n):
    wierzcholki.append(i)
  numery=G.add_nodes_from(wierzcholki)
  lista=[]
  for i in range(kroki):
    plt.title(f"Graf {rodzaj}, krok {i+1}")
    nx.draw(G,pos=poz,nodelist=wierzcholki,node_color=['#0000FF'],labels=numery)
    nx.draw(G,pos=poz,nodelist=[agent],node_color=['#FF0000'],labels = numery)
    plt.savefig("agent"+str(i)+".png")
    plt.close
    sasiedzi = list(G.neighbors(agent))
    agent=random.choice(sasiedzi)
    plik=("agent"+str(i)+".png")
    lista.append(plik)
  listagif=[]
  for i in lista:
    listagif.append(imageio.imread(i))
  imageio.mimsave(r"C:\Users\dell\Desktop\marysia\studia\programowanie\grafyLB.gif",listagif,loop=0, duration=800)
  print("koniec")
graf("B",4,0.3,2)
