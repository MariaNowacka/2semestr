from vector import *
v=Vector()
print('v: ',v)
k=Vector(4)
h=Vector(4)
k.gen()
h.gen()
print('k: ',k)
print('h: ',h)
print('v wczytane: ',v.wczyt([1,2,3]))
print('k+h: ',k+h)
print('k-h: ',k-h)
print('h*k: ',h*k)
print('h*5: ',h*5)
print(2 in v)
print(2 in k)
print('długość wektora k: ',k.dl())
print('suma elementów wektora h: ',h.suma())
print(v[1])
v.wczyt([1,2,3,4])
k+v
k*v
print(v[4])
k-v

