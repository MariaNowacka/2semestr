# lista 8
struct PeriodicMatrix{T}
M:: Matrix{T} end
function Base.getindex(P::PeriodicMatrix,i,j)
    n,m = size(P.M)
    P.M[mod1(i,n),mod1(j,m)]
end
function Base.setindex!(P::PeriodicMatrix,a,i,j)
    n,m = size(P.M)
    P.M[mod1(i,n),mod1(j,m)]=a
end
M=[1 2;
   3 4;
   5 6]
A=PeriodicMatrix(M)
A[9,9]
A[1,2]=3
A