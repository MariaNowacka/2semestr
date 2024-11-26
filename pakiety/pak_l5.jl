using Plots
## z2
r(θ)=exp(sin(θ))-2*cos(4θ)+(sin((2θ-π)/24)^5)
an = @animate for i in 1:400
    plot(r,0,i/10,proj = :polar, size=(300,300), ylimits=(0,6))
end
gif(an, fps=15)

## z3
Φ = (sqrt(5)+1)/2
t=12:400
rf(t)=t^Φ
θf(t) = 2π*Φ* t
r0=rf.(t)
Θ=θf.(t)

p=scatter(Θ, r0, linewidth=3,linecolor=:green, proj=:polar,legend=false)
for k in 1:21
    brΘ1=Θ[k:21:end]
    brR1=r0[k:21:end]
    plot!(brΘ1,brR1, proj=:polar,color=:black, label="")
end
for k in 1:13
    brΘ1=Θ[k:13:end]
    brR1=r0[k:13:end]
    plot!(brΘ1,brR1, proj=:polar,color=:black, label="")
end
p |> display
savefig("sunflower.png")

## z4
s(x)=minimum(((x-floor(x)),1-(x-floor(x))))
w=0.77
T(x)=sum(w^k*s(2^k*x) for k in 1:100)
plot(T,0,1)

## z7
using Graphs
using GraphPlot
g=Graph(100)
gplot(g)
nvertices = nv(g) # number of vertices
nedges = ne(g)    # number of edges

gplot(g, nodelabel=1:nvertices, edgelabel=1:nedges)
for e in edges(g)
  u, v = src(e), dst(e)
  println("edge $u - $v")
end
G=smallgraph(:karate)
gplot(G)
for e in edges(G)
  u, v = src(e), dst(e)
  println("edge $u - $v")
end
nodelabel = 1:nv(G)
gplot(G, nodelabel=nodelabel)
nodefillc = distinguishable_colors(nv(g), colorant"blue")
gplot(G,nodefillc=nodefillc, nodelabel=nodelabel, nodelabeldist=1.8, nodelabelangleoffset=π/4)
for i in 1:16
end
# nodes membership
membership = [1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,2,1,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2]
nodecolor = [colorant"lightseagreen", colorant"orange"]
# membership color
nodefillc = nodecolor[membership]
gplot(G, nodefillc=nodecolor,nodelabeldist=3, nodelabelangleoffset=π/4)



# https://nbviewer.orgagithub/JuliaGraphs/JuliaGraphsTutorials/blob/master/Basics.ipynb
# https://github.com/JuliaGraphs/GraphPlot.jl

'
N = 800
K = 10000
function generate_random_graph()
    A = Matrix(N, N)

    for i=1:N, j=1:N
      A[i,j] = 0
    end

    for i in sample(1:N*N, K, replace=false)
      i2s = CartesianIndices(A)
      row, col = i2s[i]
      A[row,col] = 1
      A[col,row] = 1
    end
    return A
end
function generate_random_nodes()
    nodes = Vector()
    for i= 1:N
      push!(nodes, rand() > 0.5 ? get_random_person() : get_random_address())
    end
    nodes
  end
  function convert_to_graph(A, nodes)
    N = length(nodes)
    push!(graph, map(n -> GraphVertex(n, GraphVertex[]), nodes)...)
  
    for i = 1:N, j = 1:N
        if A[i,j] == 1
          push!(graph[i].neighbors, graph[j])
        end
    end
  end
A = generate_random_graph()
nodes = generate_random_nodes()
convert_to_graph(A, nodes)
'