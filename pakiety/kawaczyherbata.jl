using Graphs
using GraphPlot
using Colors
g = smallgraph(:karate)
gplot(g)
nodelabel = 1:nv(g)
gplot(g, nodelabel=nodelabel)
gplot(g, nodelabel=nodelabel, nodelabeldist=1.500)
edgelabel = 1:Graphs.ne(g)
gplot(g, edgelabel=edgelabel, nodelabel=nodelabel, edgelabeldistx=0.5, edgelabeldisty=0.5)
membership=rand((1,2),nv(g))
nodecolor = [colorant"lightseagreen", colorant"orange"]
nodefillc = nodecolor[membership]
gplot(g, nodefillc=nodefillc)
for e in edges(g)
  u, v = src(e), dst(e)
  println("edge $u - $v")
end
edges(g)
locs_x, locs_y = spring_layout(g)
gplot(g,locs_x, locs_y,odelabel=nodelabel)
layout=(args...)->spring_layout(args...; C=10)
gplot(g, layout=spring_layout, nodelabel=nodelabel, nodefillc=nodefillc)
d=Dict(0 => 0)
for i in edges(g)
  d[src(i)]=dst(i)
end
gplot(g, layout=circular_layout, nodelabel=nodelabel,nodefillc=nodefillc)
#= i need help
znajomości = 
tablica czy coś ze znajomościami, jeśli ileś znajomych jest w opozycji, 
to w czasie x zmieni obóz - jak zmienić kolor jednego noda -> to można zmienić w membership po prostu? =#
a=adjacency_matrix(g)